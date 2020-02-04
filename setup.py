#!/usr/bin/env python

from setuptools import setup


setup(
    name='applescript',
    author='daveb@smurfless.com',
    versioning='dev',
    setup_requires=['setupmeta'],
    dependency_links=['https://pypi.org/project/setupmeta'],
    packages=["applescript"],
    include_package_data=True,
    python_requires='>=3.4',
    install_requires=[],
    extras_require={
        'dev': [
            'behave',
            'flake8',
            'invoke',
            'tox',
            'pytest'
        ]
    },
)
