#! /usr/bin/env python

from distutils.core import setup
from glob import glob
print(glob("*"))
setup(
    name = 'rainbow-shooter',
    version = '0.1',
    description = 'color slideshow.',
    author = 'Damjan Dimitrioski',
    author_email = 'damjandimitrioski@gmail.com',
    url = '',
    license = 'GPL',
    platforms = 'posix',
    data_files=[('share', ['rainbow_shooter.xml'])],
    packages = ['rainbow-shooter'],
    )
