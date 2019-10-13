"""
Activate a virtual environment from Python.

Activation logic taken from https://github.com/pypa/virtualenv
"""

import os
import site
import sys


def is_venv():
    """Return true if a virtual environment is active."""
    is_conda_env = getattr(sys, "base_prefix", sys.prefix) != sys.prefix
    is_virtualenv = hasattr(sys, "real_prefix")
    return is_conda_env or is_virtualenv


def activate_venv(venv=None):
    """
    Search and activate a Virtual Environment.

    Activate the virtual environment from:
    - The `venv` param, if one is given.
    - `VIRTUAL_ENV` environmental variable if set.
    - a `.venv` folder in the current working directory
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
    """Activate a Virtual Environment if one is not active."""
    if is_venv():
        # pylint was invoked from within a venv.  Nothing to do.
        return

    activate_venv(venv)
