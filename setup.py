#!/usr/bin/env python

from distutils.core import setup

setup(name = 'HACluster',
      version = '0.2',
      description = 'Hierarchical Agglomerative Cluster Analysis in Python',
      author = 'Folgert Karsdorp',
      author_email = 'folgert.karsdorp@inl.nl',
      copyright = 'Instituut voor Nederlandse Lexicologie',
      requires = ['numpy'],
      url = "https://github.com/fbkarsdorp/HAC-python",
      packages = ['HACluster'],
      platforms = 'Mac OS X, MS Windows, GNU Linux')
