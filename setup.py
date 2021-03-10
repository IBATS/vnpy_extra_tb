#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author  : MG
@Time    : 2018/6/14 16:07
@File    : setup.py
@contact : mmmaaaggg@163.com
@desc    : 
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as rm:
    long_description = rm.read()
packages = find_packages(exclude=['scripts', 'scripts.*'])
setup(name='vnpy_extra_tb',
      version='0.1.20210311.0',
      description='该项目主要用于在vnpy框架下扩展部分 Trade Blazer (TB) 的函数包，以方便部分TB程序的迁移使用。',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='MG',
      author_email='mmmaaaggg@163.com',
      url='https://github.com/IBATS/vnpy_extra_tb',
      packages=packages,
      python_requires='>=3.7',
      classifiers=(
          "Programming Language :: Python :: 3 :: Only",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: Unix",
          "Operating System :: POSIX",
          "License :: OSI Approved :: MIT License",
          "Development Status :: 5 - Production/Stable",
          "Environment :: No Input/Output (Daemon)",
          "Intended Audience :: Developers",
          "Natural Language :: Chinese (Simplified)",
          "Topic :: Software Development",
      ),
      install_requires=[
          'vnpy_extra>=0.6.0.0',
      ])
