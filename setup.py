#!/usr/bin/env python
__author__ = 'mca18'
import os
import sys

from setuptools import setup

if sys.argv[-1] == 'publish':
  os.system('python setup.py sdist upload')
  sys.exit()

PACKAGES = [
  'namespaces',
]

REQUIRES = [
  'argh >= 0.26.1',
  'python-novaclient >= 2.20.0',
  'python-cinderclient >= 1.1.1',
  'python-glanceclient >= 0.15.0',
  'python-heatclient >= 0.2.12',
  'python-keystoneclient >= 1.0.0',
  'python-neutronclient >= 2.3.10',
]

with open('README.md', 'r') as f:
  README = f.read()

with open('HISTORY', 'r') as f:
  HISTORY = f.read()

setup(
  name='namespaces',
  version='0.0.1',
  description='Neutron agent namespace check',
  long_description=README + '\n\n' + HISTORY,
  author='Max Cameron',
  author_email='maxwell.cameron@bskyb.com',
  url='http://github.com/sky-shiny/namespaces',
  packages=PACKAGES,
  package_data={
    '': ['LICENSE'],
  },
  scripts=['ns'],
  include_package_data=True,
  install_requires=REQUIRES,
  license='BSD License',
  zip_safe=False,
  classifiers=(
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7'
  ),
)
