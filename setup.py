#!/usr/bin/env python

from setuptools import setup


setup(
    name='lameapplescript',
    author='daveb@smurfless.com',
    url='https://github.com/smurfless1/applescript',
    versioning='dev',
    setup_requires=['setupmeta'],
    dependency_links=['https://pypi.org/project/setupmeta'],
    packages=["lameapplescript"],
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
