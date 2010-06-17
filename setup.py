"""
Rainbow-shooter
========

{Rainbow-shooter long description}

{Link to binaries}


Features
--------

- item 1
- item 2


Development Version
-------------------

Link to git
"""
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='Rainbow_shooter',
    version='0.1',
    url='http://github.com/gnud/rainbow-shooter',
    license='GPL',
	author='Damjan Dimitrioski',
	author_email='damjandimitrioski@gmail.com',
    description='A slideshow that show colors from a list in fullscreen.',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Users',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=['rainbow_shooter'],
    package_data={
        'rainbow-shooter.share/': ['ui/*']
    },
    platforms='any'
)
