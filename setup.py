#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='glamkit-performance',
    version='0.5.2',
    description='A template tag to help with concurrent media serving from Django',
    author='Thomas Ashelford',
    author_email='thomas@interaction.net.au',
    url='http://glamkit.org/',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)