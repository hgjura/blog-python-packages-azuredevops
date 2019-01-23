from setuptools import setup, find_packages
import io
import os
import sys

VERSION = '0.0.0.2' #required - for example 0.1.0.1
NAME = 'mdw'
AUTHOR = 'Darth Vedar'
AUTHOR_EMAIL = 'dvedar@deathstar.gov'
DESCRIPTION = ''
PROJECT_URL = 'http://github.com/someurl'
LICENSE = 'Restricted' #could be MIT License, or Restricted

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=PROJECT_URL,
    license=LICENSE,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]   
)