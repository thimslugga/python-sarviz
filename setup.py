#!/usr/bin/env python

from distutils.core import setup

setup(name='sar',
      version='0.0.1',
      description='SAR (sysstat) output files parser and visualizer',
      author='Adam Kaminski <adam@adamkaminski.com>',
      url='https://github.com/thimslugga/python-sarviz',
      packages=['sar'],
      install_requires=[
          'matplotlib',
      ],
      license='LGPL',
      platforms=['linux'])
