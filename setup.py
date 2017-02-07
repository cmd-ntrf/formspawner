#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import os
import sys

from setuptools import setup

setup_args = dict(
    name                = 'formspawner',
    packages            = ['formspawner'],
    version             = '0.1',
    description         = "Formspawner: A Jupyterhub plugin to add options form functionality to any spawner.",
    long_description    = "",
    author              = "Félix-Antoine Fortin",
    author_email        = "felix-antoine.fortin@calculquebec.ca",
    install_requires    = ['wtforms', 'jinja2', 'traitlets'],
    license             = "BSD",
    platforms           = "Linux, Mac OS X",
    keywords            = ['Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)

def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()
