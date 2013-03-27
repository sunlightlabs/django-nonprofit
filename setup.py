#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-nonprofit',
    version='0.2',
    author='Jeremy Carbaugh',
    author_email='jcarbaugh@sunlightfoundation.com',
    description='Django app for managing and publishing basic information related to a non-profit organization.',
    long_description=open("README.rst").read(),
    url='http://github.com/sunlightlabs/django-nonprofit/',
    license='BSD',
    packages=find_packages(),
    package_data={
        'nonprofit.mailroom': ['templates/mailroom/*']
    },
    install_requires=[
        "PIL",
        "South == 0.7.6",
        "tablib == 0.9.11",
        "django-tablib == 2.4.1",
        "django-tastypie == 0.9.14",
        "django-humanity == 0.2",
    ],
)
