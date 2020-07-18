#!/usr/bin/env python

import io
import os
import re

from setuptools import setup, find_packages

install_requires = [
    r.strip() for r in open('requirements.txt')
    if r.strip() and not r.strip().startswith('#')
]


def get_long_desc():
    with io.open('README.md', encoding='utf-8') as fp:
        desc = fp.read()
    desc += '\n\n'
    with io.open('CHANGES', encoding='utf-8') as fp:
        desc += fp.read()
    return desc


def get_version():
    return '0.1'

setup(
    name='broker',
    version=get_version(),
    description='Faust Kafka broker.',
    long_description=get_long_desc(),
    maintainer='Will Kahn-Greene',
    maintainer_email='dmitryro@gmail.com',
    url='https://github.com/dmitryro/broker.git',
    license='Apache Software License',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.rst']},
    zip_safe=False,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
