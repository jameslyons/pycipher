.. pycipher documentation master file, created by
   sphinx-quickstart on Sat Feb 08 18:44:38 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pycipher's documentation!
====================================

.. toctree::
   :maxdepth: 2
   
Common classical ciphers implemented in Python.

The code is hosted on GitHub: https://github.com/jameslyons/pycipher

If you find any bugs make an issue or create a pull request.

Example usage
-------------

::

    >>> from pycipher import ADFGVX
    >>> adfgvx = ADFGVX(key='PH0QG64MEA1YL2NOFDXKR3CVS5ZW7BJ9UTI8', keyword='GERMAN')
    >>> adfgvx.encipher("Hello world!")
    'FVFDAGXAFFFFGFAGADFG'
    >>> adfgvx.decipher(_)
    'HELLOWORLD'

.. contents:: Table of Contents
   :depth: 2
    
A Short Aside on Keysquares
----------------------------
Many of the ciphers mentioned here e.g. :py:meth:`pycipher.Playfair`, :py:meth:`pycipher.Foursquare` use keysquares as part of their key information. A keysquare looks like this::

    Z G P T F
    O I H M U
    W D R C N
    Y K E Q A
    X V S B L

The keysquare above is a 5 by 5 keysquare consisting of 25 characters. To use this keysquare as part of a key, read each row starting with the top row, then the second row etc. The keysquare above
becomes "ZGPTFOIHMUWDRCNYKEQAXVSBL". Note that with only 25 characters, 1 character can't be included. This is usually the letter 'J', wherever this letter appears it is
replaced by 'I'.

Keysquares can also be 6 by 6. In this case the 26 letters A-Z plus the 10 numbers 0-9 are used. An example of this sort of keysquare is::

    p h 0 q g 6
    4 m e a 1 y
    l 2 n o f d
    x k r 3 c v
    s 5 z w 7 b
    j 9 u t i 8
    
The keysquare above becomes "ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8".
    
The Ciphers
===========

ADFGX Cipher
------------
This cipher uses a keysquare as part of its key, see `A Short Aside on Keysquares`_ for information.

.. autoclass:: pycipher.ADFGX
   :members:
   
ADFGVX Cipher
-------------
This cipher uses a keysquare as part of its key, see `A Short Aside on Keysquares`_ for information.

.. autoclass:: pycipher.ADFGVX
   :members:
   
Affine Cipher
-------------
.. autoclass:: pycipher.Affine
   :members:

Autokey Cipher
--------------
.. autoclass:: pycipher.Autokey
   :members:

Atbash Cipher
--------------
.. autoclass:: pycipher.Atbash
   :members:
   
Beaufort Cipher
---------------
.. autoclass:: pycipher.Beaufort
   :members:

Bifid Cipher
--------------
This cipher uses a keysquare as part of its key, see `A Short Aside on Keysquares`_ for information.

.. autoclass:: pycipher.Bifid
   :members:

Caesar Cipher
--------------
.. autoclass:: pycipher.Caesar
   :members:

Columnar Transposition Cipher
-----------------------------
.. autoclass:: pycipher.ColTrans
   :members:

Enigma M3 Cipher
----------------
The Enigma M3 was used by the German army during the Second World War. The keying information for mechanical ciphers can be a little more complicated
than for the simpler ciphers, it may be beneficial to read `this guide <http://www.practicalcryptography.com/ciphers/enigma-cipher/>`_ to get an
understanding of how the Enigma works before using it.

.. autoclass:: pycipher.Enigma
   :members:

Foursquare Cipher
-----------------
This cipher uses a keysquare as part of its key, see `A Short Aside on Keysquares`_ for information.

.. autoclass:: pycipher.Foursquare
   :members:

Gronsfeld Cipher
-----------------
.. autoclass:: pycipher.Gronsfeld
   :members:

M-209 Cipher
----------------
The M-209 was used by the American army during the Second World War. The keying information for mechanical ciphers can be a little more complicated
than for the simpler ciphers, it may be beneficial to read `this page <http://en.wikipedia.org/wiki/M-209>`_ , in particular the parts about "Example Configuration" to get an
understanding of how the M-209 works before using it.

.. autoclass:: pycipher.M209
   :members:
   
Playfair Cipher
-----------------
This cipher uses a keysquare as part of its key, see `A Short Aside on Keysquares`_ for information.

.. autoclass:: pycipher.Playfair
   :members:   
   
Polybius Square Cipher
----------------------
This cipher uses a keysquare as part of its key, see `A Short Aside on Keysquares`_ for information.

.. autoclass:: pycipher.PolybiusSquare
   :members:

Porta Cipher
--------------
.. autoclass:: pycipher.Porta
   :members:
   
Railfence Cipher
--------------
.. autoclass:: pycipher.Railfence
   :members:

Rot13 Cipher
--------------
.. autoclass:: pycipher.Rot13
   :members:

Simple Substitution Cipher
--------------------------
.. autoclass:: pycipher.SimpleSubstitution
   :members:

Vigenere Cipher
-----------------
.. autoclass:: pycipher.Vigenere
   :members:
   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

