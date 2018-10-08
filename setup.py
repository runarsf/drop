import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "punct",
    version = "1.0",
    author = "Runar Fredagsvik",
    author_email = "runar.fredagsvik@gmail.com",
    description = ("A simple todo-list manager."),
    license = "MIT",
    keywords = "todo open-source",
    url = "http",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

