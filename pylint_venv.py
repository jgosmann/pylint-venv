"""
Allow a globally installed Pylint to lint an (active) virtual or Conda
environment.

If a globally installed Pylint is invoked from an active virtualenv or Conda
environment, add the environment's paths to Pylint.

If no virtualenv is active but the CWD contains a virtualenv in a  ``.venv``
folder, activate that env and add its paths to Pylint.

Do nothing if no virtualenv is active or if Pylint is installed within the
active virtualenv.

Activation logic taken from https://github.com/pypa/virtualenv

Usage:

- Add an init hook to your ``.pylintrc``::
    init-hook=
        try: import pylint_venv
        except ImportError: pass
        else: pylint_venv.inithook()

- Add the init hook as command line argument::

    pylint --init-hook="import pylint_venv; pylint_venv.inithook()"

- Add the init hook as command line argument and explicitly pass a venv::

    pylint --init-hook="import pylint_venv; pylint_venv.inithook('$(pwd)/env')"

"""

import os
import platform
import site
import sys


IS_WIN = platform.system() == "Windows"
IS_PYPY = platform.python_implementation() == "PyPy"


def is_venv():
    """Return ``true`` if a virtual environment is active and Pylint is
    installed in it.

    """
    is_conda_env = getattr(sys, "base_prefix", sys.prefix) != sys.prefix
    is_virtualenv = hasattr(sys, "real_prefix")
    return is_conda_env or is_virtualenv


def detect_venv():
    # Check for a virtualenv or Conda env
    for var in ["VIRTUAL_ENV", "CONDA_PREFIX"]:
        venv = os.getenv(var, "")
        if venv:
            return venv

    # Check if a local ".venv" folder exists
    cwd = os.getcwd()
    exec_path = "Scripts" if IS_WIN else "bin"
    if os.path.isfile(os.path.join(cwd, ".venv", exec_path, "activate")):
        return os.path.join(cwd, ".venv")

    return None


def activate_venv(venv):
    """Check for an active venv and add its paths to Pylint.

    Activate the virtual environment from:

    - The *venv* param if one is given.
    - ``VIRTUAL_ENV`` environmental variable if set.
    - A ``.venv`` folder in the current working directory

    """
    if IS_PYPY:
        site_packages = os.path.join(venv, "site-packages")
    elif IS_WIN:
        site_packages = os.path.join(venv, "Lib", "site-packages")
    else:
        pyver = f"python{sys.version_info[0]}.{sys.version_info[1]}"
        site_packages = os.path.join(venv, "lib", pyver, "site-packages")

    prev = set(sys.path)
    site.addsitedir(site_packages)
    sys.real_prefix = sys.prefix
    sys.prefix = venv

    # Move the added items to the front of sys.path (in place!)
    new = list(sys.path)
    new_paths = [i for i in new if i not in prev]
    kept_paths = [i for i in new if i in prev]
    sys.path[:] = new_paths + kept_paths


def inithook(venv=None):
    """Add a virtualenv's paths to Pylint.

    Use the environment *env* if set or auto-detect an active virtualenv.

    """
    if is_venv():
        # pylint was invoked from within a venv.  Nothing to do.
        return

    if venv is None:
        venv = detect_venv()

    if venv is None:
        return

    print(f"\033[1;33mUsing env: {venv}\033[0m", file=sys.stderr)
    activate_venv(venv)
