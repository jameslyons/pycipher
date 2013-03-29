pycipher
========

Common classical ciphers implemented in Python.


Install
-------

::

    pip install git+git://github.com/jameslyons/pycipher


Example usage
-------------

::

    >>> from pycipher import ADFGVX
    >>> adfgvx = ADFGVX(key='PH0QG64MEA1YL2NOFDXKR3CVS5ZW7BJ9UTI8', keyword='GERMAN')
    >>> adfgvx.encipher("Hello world!")
    'FVFDAGXAFFFFGFAGADFG'
    >>> adfgvx.decipher(_)
    'HELLOWORLD'


Feedback
--------

The code is hosted on GitHub: https://github.com/jameslyons/pycipher

If you find any bugs make an issue or create a pull request.

To run the test suite::

    python setup.py test

