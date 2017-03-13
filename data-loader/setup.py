#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_requirements = parse_requirements('requirements.txt', session=False)

# requirements is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
requirements = [str(ir.req) for ir in install_requirements]

setup(
        name='ContractAnalyser',
        version='0.0.1',
        description='Analyse Solidity contracts from a DB',
        author='Dominik Harz',
        author_email='dominik.harz@gmail.com',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 2.7',
        ],
        packages=find_packages(exclude=['contrib', 'docs', 'tests']),
        install_requires=requirements,
        include_package_data = True,
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
      )
