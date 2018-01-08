# -*- coding: utf-8 -*-
"""
    Setup
    -----

    Enables the ``setuptools`` to build and install the package

"""

import codecs
from setuptools import setup

# README into long description
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name="bagels-theme",
    description="Bagels Sphinx Documentation Theme",
    long_description=readme,
    version="0.1.0",
    author="Bryant Biggs",
    author_email="bryantbiggs@gmail.com",
    url="https://github.com/bryantbiggs/bagels_theme",
    license="LICENSE",
    install_requires=[],
    include_package_data=True,
    packages=["bagels_theme"],
    package_data={},
    entry_points={
        "sphinx.html_themes": [
            "bagels_theme = bagels_theme",
        ]
    },
    classifiers=[
        "Development Status :: 0 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
