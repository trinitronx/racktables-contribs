import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rtapi",
    version = "0.1.2",
    author = "Robert Vojcik",
    author_email = "robert@vojcik.net",
    description = ("Racktables API"
                   "Python module for accessing and manipulating racktables objects."),
    license = "GPLv2",
    keywords = "racktables api rtapi",
    url = "http://packages.python.org/rtapi",
    packages=['rtapi'],
    long_description=read('README.md'),
    install_requires=[
        'ipaddr',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
    ]
)
