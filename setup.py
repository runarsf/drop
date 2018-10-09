# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
import os
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('punct/punct.py').read(),
    re.M
    ).group(1)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "punct",
    packages = ["punct"],
    entry_points = {
        "console_scripts": ['punct = punct.punct:main']
	},
    version = version,
    description = ("A simple todo-list manager."),
    long_description=read('README.rst'),
    author = "Runar Fredagsvik",
    author_email = "runarsf@protonmail.com",
    url = "https://github.com/runarsf/punct",

    keywords = "todo open-source",
    license = "MIT",
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: End Users/Desktop",
    ],
)

