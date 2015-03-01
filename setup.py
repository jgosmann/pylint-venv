#!/usr/bin/env python

from distutils.core import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name='pylint-venv',
    version='1.0',
    description='pylint-venv provides a Pylint init-hook to use the same '
    'Pylint installation with different virtual environments.',
    long_description=long_description,
    author='Jan Gosmann',
    author_email='jan@hyper-world.de',
    url='https://github.com/jgosmann/pylint-venv/',
    py_modules=['pylint_venv'],
    provides=['pylint_venv'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ]
)
