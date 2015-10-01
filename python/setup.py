#!/usr/bin/env python

"""
Wordlist python module setuptools script
"""

from os import path
from setuptools import setup, find_packages

_pkg_name = 'wordlist'
_pkg_version = '0.1'
_pkg_reqs = file(path.join(path.realpath(path.dirname(__file__)), 'requirements.txt')).readlines()

setup(name=_pkg_name,
      version=_pkg_version,
      description='Utilities to access and create lists of words',
      author='Shahar Evron',
      author_email='shahar.evron@gmail.com',
      url='https://github.com/shevron/wordlists',
      packages=find_packages(),
      install_requires=_pkg_reqs,
      scripts=[])
