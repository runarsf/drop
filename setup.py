import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "punct",
    version = "1.0.1",
    author = "Runar Fredagsvik",
    author_email = "runarsf@protonmail.com",
    description = ("A simple todo-list manager."),
    license = "MIT",
    keywords = "todo open-source",
    url = "https://github.com/runarsf/punct",
    py_modules = ["punct"],
    # packages=['os', 'sys', 'subprocess'],
    long_description=read('README.md'),
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    entry_points='''
        [console_scripts]
        punct=punct:main
    ''',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: End Users/Desktop",
    ],
)

