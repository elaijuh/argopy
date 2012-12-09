#!/usr/bin/env python

from distutils.core import setup
from argo import __version__

setup(name = 'argo',
      version = argopy.__version__,
      description = 'Python SDK for Argo BBS',
      long_description = open('README.md', 'r').read(),
      author = '@mopodo',
      author_email = 'hjiale@gmail.com',
      url = 'https://github.com/mopodo/argopy',
      download_url = 'https://github.com/mopodo/argopy',
      py_modules = ['argo'],
      classifiers = [
        'Development Status :: 1 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ]
     )
