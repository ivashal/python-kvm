# -*- coding: utf-8 -*-
from distutils.core import setup

setup (
    name='Python remote KVM manager',
    version='0.1',
    author='François Ménabé',
    author_email='francois.menabe@gmail.com',
    packages=['kvm'],
    licence='LICENCE.txt',
    description='An API for managing KVM host.',
    long_description=open('README.txt').read(),
    install_requires=[
        'unix'
    ],
)
