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

Add the following to your ``~/.pylintrc``:

.. code:: ini

    init-hook=
        try: import pylint_venv
        except ImportError: pass
        else: pylint_venv.inithook()

The hook will then be used automatically if

- a virtualenv is activated

- a Conda environment is activated

- no env is activated but your CWD contains a virtualenv in ``.venv``

and if pylint is not installed in that env, too.

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

.. _Pylint: http://www.pylint.org/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
