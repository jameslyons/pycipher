#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='pycipher',
    version='0.1',
    description='Several simple cipher algorithms',
    author='James Lyons',
    author_email='james.lyons0@gmail.com',
    #url='https://private.pypi.enigmainteractive.net.au.private/pypi/django-console/',

    packages=find_packages(exclude=['tests','tests.*']),
    include_package_data=True,  # declarations in MANIFEST.in
    test_suite='tests',
    #install_requires=['Django>=1.2', 'django-restful>=0.1.1'],

    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)