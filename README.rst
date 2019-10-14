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


You can also call the hook via a command line argument.  This way you can also
pass an explicit env. to use:

.. code:: console

    $ pylint --init-hook="import pylint_venv; pylint_venv.inithook()"
    $ pylint --init-hook="import pylint_venv; pylint_venv.inithook('$(pwd)/env')"

.. _Pylint: http://www.pylint.org/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
