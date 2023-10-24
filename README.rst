.. image:: https://github.com/jgosmann/pylint-venv/actions/workflows/ci.yml/badge.svg
  :target: https://github.com/jgosmann/pylint-venv/actions/workflows/ci.yml
  :alt: CI and release pipeline
.. image:: https://img.shields.io/pypi/v/pylint-venv
  :target: https://pypi.org/project/pylint-venv/
  :alt: PyPI
.. image:: https://img.shields.io/pypi/pyversions/pylint-venv
  :target: https://pypi.org/project/pylint-venv/
  :alt: PyPI - Python Version
.. image:: https://img.shields.io/pypi/l/pylint-venv
  :target: https://pypi.org/project/pylint-venv/
  :alt: PyPI - License


pylint-venv
===========

Pylint_ does not respect the currently activated virtualenv_ if it is not
installed in every virtual environment individually.  This module provides
a Pylint init-hook to use the same Pylint installation with different virtual
environments.

Installation
------------

.. code:: bash

    pip install pylint-venv
    
Add the hook to your Pylint configuration. See the section below corresponding
to the type of configuration file you use.

Configure with ``pyproject.toml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the following to your ``pyproject.toml``:

.. code:: toml
   
    [tool.pylint.MAIN]
    init-hook = """
    try: import pylint_venv
    except ImportError: pass
    else: pylint_venv.inithook()
    """


Configure with ``.pylintrc``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the following to your ``.pylintrc``:

.. code:: ini

    [MAIN]
    init-hook=
        try: import pylint_venv
        except ImportError: pass
        else: pylint_venv.inithook()
        
If you add this to your ``~/.pylintrc`` in your home directory, it will be
applied to all projects by default.

        
Usage
-----

The hook will then be used automatically if

- a virtualenv without pylint is active,

- or a Conda environment without pylint is active,

- or no environment is active but your CWD contains virtualenv directory.

Anything listed in the ``PYLINT_VENV_PATH`` environment variable is considered
a virtualenv directory. The default, if the variable is unset, is `.venv`. Use
a colon (`:`) as path separator. Example for checking directories ``.venv`` and
``.virtualenv``:

.. code:: console

    PYLINT_VENV_PATH=.venv:.virtualenv

You can also call the hook via a command line argument:

.. code:: console

    $ pylint --init-hook="import pylint_venv; pylint_venv.inithook()"

This way you can also explicitly set an environment to be used:

.. code:: console

    $ pylint --init-hook="import pylint_venv; pylint_venv.inithook('$(pwd)/env')"

If ``pylint`` itself is installed in a virtualenv, then you can ignore it by passing
``force_venv_activation=True`` to force the activation of a different virtualenv:

.. code:: console

    $ pylint --init-hook="import pylint_venv; pylint_venv.inithook(force_venv_activation=True)"


This will try to automatically detect virtualenv and activate it.


Troubleshooting
---------------

General
^^^^^^^

pylint_venv fails to import
"""""""""""""""""""""""""""

Most likely pylint-venv is not installed in the same virtual environment as
pylint. Either make sure to ensure pylint-venv into the same virtual environment
as pylint, or add the appropriate path in the init hook:

.. code:: python

    import sys
    sys.path.append("/path/to/installation/folder/of/pylint_venv")


pylint_venv breaks parsing with tools
"""""""""""""""""""""""""""""""""""""

When tools call pylint with :code:`-f json`, an extra line may break the parser, as the 
output is no longer valid json. To avoid printing "using venv ...", pass :code:`quiet=True`
to :code:`inithook`

.. code:: console

   $ pylint -f json --init-hook="import pylint_venv; pylint_venv.inithook(quiet=True)"


Virtual environment does not get used (installed modules are reported as 'unable to import')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Most likely the virtual environment does not get activated because pylint itself
runs in a virtual environment. You can force the activation of the virtual
environment with the :code:`force_venv_activation=True` flag to the
:code:`pylint_venv.inithook` function.


Homebrew
^^^^^^^^

Homebrew installs pylint into a separate virtual environment, thus you will
need to set the `force_venv_activation=True` flag. This also means, that
pylint_venv will be in a different search path and you must add the proper
path to `sys.path`. You can use the following configuration adjusted to your
Python version:

.. code:: ini

    [MAIN]
    init-hook=
        import sys
        sys.path.append("/usr/local/lib/python3.8/site-packages")
        try: import pylint_venv
        except ImportError: pass
        else: pylint_venv.inithook(force_venv_activation=True)


.. _Pylint: http://www.pylint.org/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
