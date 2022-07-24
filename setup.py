from setuptools import setup
import codecs
import os

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='get_files',
    version=get_version("get_files/__init__.py"),
    description='Python package that provides a utility function to recursively get files that match a pattern',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LucaAngioloni/get_files',
    author='Luca Angioloni',
    author_email='lucaangioloni@gmail.com',
    license='MIT License',
    packages=['get_files'],
    keywords=["files", "get_files", "recursive", "pattern", "match"],
    classifiers=[
        'Intended Audience :: Developers',
        "Intended Audience :: Other Audience",
        "Intended Audience :: System Administrators",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
)
