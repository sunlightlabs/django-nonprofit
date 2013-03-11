#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='django-nonprofit',
      version='0.1.0',
      description='Django app for managing and publishing basic information related to a non-profit organization.',
      author='Jeremy Carbaugh',
      author_email='jcarbaugh@sunlightfoundation.com',
      license='BSD',
      url='http://github.com/sunlightlabs/django-nonprofit/',
      packages=find_packages(),
      # The wildcard ignores hidden files
      package_data={
          'nonprofit.mailroom': ['templates/mailroom/*']
      }
     )
