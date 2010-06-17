#!/usr/bin/env python

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

import os

from setuptools import setup


PROJECT = u'rainbow_shooter'
VERSION = '0.1'
URL = 'http://github.com/gnud/rainbow-shooter'
AUTHOR = u'Damjan Dimitrioski'
AUTHOR_EMAIL = u'damjandimitrioski@gmail.com'
DESC = "A slideshow that show colors from a list in fullscreen."

def read_file(file_name):
    file_path = os.path.join(
        os.path.dirname(__file__),
        file_name
        )
    return open(file_path).read()

setup(
    name=PROJECT,
    version=VERSION,
    description=DESC,
    long_description=read_file('README.rst'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=read_file('LICENSE'),
    namespace_packages=[],
    packages=[u'rainbow_shooter'],
    package_dir = {'': os.path.dirname(__file__)},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Requirements -*-
    ],
    entry_points = {
        # -*- Entry points -*-
    },
    classifiers=[
    	# see http://pypi.python.org/pypi?:action=list_classifiers
        # -*- Classifiers -*-
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        "Programming Language :: Python",
    ],
)
