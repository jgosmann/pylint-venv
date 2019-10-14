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

"""

import os
import site
import sys


def is_venv():
    """Return ``true`` if a virtual environment is active and Pylint is
    installed in it.

    """
    is_conda_env = getattr(sys, "base_prefix", sys.prefix) != sys.prefix
    is_virtualenv = hasattr(sys, "real_prefix")
    return is_conda_env or is_virtualenv


def activate_venv(venv=None):
    """Check for an active venv and add its paths to Pylint.

    Activate the virtual environment from:

    - The *venv* param if one is given.
    - ``VIRTUAL_ENV`` environmental variable if set.
    - A ``.venv`` folder in the current working directory

    """
    if venv is None:
        venv = os.environ.get("VIRTUAL_ENV", None)

    if venv is None:
        cwd = os.getcwd()
        exec_path = 'Scripts' if sys.platform == "win32" else 'bin'
        if os.path.isfile(os.path.join(cwd, ".venv", exec_path, "activate")):
            venv = os.path.join(cwd, ".venv")

    if venv is not None:
        os.environ["VIRTUAL_ENV"] = venv
        os.environ["PATH"] = (
            os.path.join(venv, "bin") + os.pathsep + os.environ.get("PATH", "")
        )
        base = venv
        if sys.platform == "win32":
            site_packages = os.path.join(base, "Lib", "site-packages")
        else:
            site_packages = os.path.join(
                base, "lib", "python%s" % sys.version[:3], "site-packages"
            )

        prev = set(sys.path)
        site.addsitedir(site_packages)
        sys.real_prefix = sys.prefix
        sys.prefix = base

        # Move the added items to the front of sys.path (in place!)
        new = list(sys.path)
        sys.path[:] = [i for i in new if i not in prev] + [i for i in new if i in prev]


def inithook(venv=None):
    """Add a virtualenv's paths to Pylint.

    Use the environment *env* if set or auto-detect an active virtualenv.

    """
    if is_venv():
        # pylint was invoked from within a venv.  Nothing to do.
        return

    activate_venv(venv)
