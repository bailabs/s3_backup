# -*- coding: utf-8 -*-
# imports - standard imports
from setuptools import setup, find_packages
import re
import ast
import os

# get version from __version__ variable in frappe/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

with open('s3_backup/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='s3_backup',
    version=version,
    description='Use Amazon S3 Backup for Frappe and ERPNext',
    author='Chris Ian Fiel',
    author_email='ccfiel@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)


