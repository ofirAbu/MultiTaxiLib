# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 2021

@author: Ofir
"""

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='MultiTaxiEnv',
    url='https://github.com/ofirAbu/MultiTaxiLib/tree/master/MultiTaxiLib',
    author='Ofir Abu, Howie Guo, Kevin Huang and Sarah Keren',
    # Needed to actually package something
    packages=['MultiTaxiLib'],
    # Needed for dependencies
    install_requires=['numpy','gym'],
    # *strongly* suggested for sharing
    version='0.3',
    # The license can be anything you like
    license='None',
    description='Multi Agent Taxis Environment',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
