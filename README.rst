pylint-venv
===========

Pylint_ does not respect the currently activated virtualenv_ if it is not
installed in every virtual environment individually. This module provides
a Pylint init-hook to use the same Pylint installation with different virtual
environments.

Installation
------------

.. code:: bash

    pip install pylint-venv

Add the following to your ``~/.pylintrc``:

.. code:: ini

    init-hook="
        from pylint_venv import inithook
        inithook()"

.. _Pylint: http://www.pylint.org/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
