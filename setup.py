from setuptools import setup


setup(
    name='pylint-venv',
    version='2.1.0',
    description=(
        'pylint-venv provides a Pylint init-hook to use the same Pylint '
        'installation with different virtual environments.'
    ),
    long_description=open('README.rst').read(),
    author='Jan Gosmann, Federico Jaramillo',
    author_email='jan@hyper-world.de, federicojaramillom@gmail.com',
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)
