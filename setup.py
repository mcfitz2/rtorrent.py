import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rtorrent",
    version = "0.0.0",
    author = "Micah Fitzgerald",
    author_email = "mcfitz2@gmail.com",
    description = ("Library for easy access to the Rtorrent XMLRPC API"),
    license = "GPLv2",
    keywords = "rtorrent xmlrpc",
    packages=['rtorrent'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)
