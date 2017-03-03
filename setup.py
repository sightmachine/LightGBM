# coding: utf-8
# pylint: disable=invalid-name, exec-used
"""Setup lightgbm package."""
from __future__ import absolute_import

import glob
import os
import sys

from setuptools import Extension, find_packages, setup

sys.path.insert(0, '.')

LIB_SOURCE_GLOBS = [
    "src/application/*.cpp",
    "src/boosting/*.cpp",
    "src/io/*.cpp",
    "src/metric/*.cpp",
    "src/objective/*.cpp",
    "src/network/*.cpp",
    "src/treelearner/*.cpp",
    "src/c_api.cpp",
]
LIB_SOURCES = []
for pattern in LIB_SOURCE_GLOBS:
    for path in glob.glob(pattern):
        LIB_SOURCES.append(path)

shared_lib = Extension(
    'lightgbm',
    define_macros = [('MAJOR_VERSION', '1'), ('MINOR_VERSION', '0')],
    include_dirs = ["include"],
    sources = LIB_SOURCES,
)

# TODO: Make this work just as well on OSX and Windows.
shared_lib.extra_compile_args = [
    '-pthread', '-O3', '-Wall', '-std=c++11', '-DUSE_SOCKET', '-fPIC',
    '-Wno-unknown-pragmas',
]

setup(name='lightgbm',
      version="20170301.1+sm1",
      description="LightGBM Python Package",
      install_requires=[
          'numpy',
          'scipy',
      ],
      maintainer='Sight Machine',
      maintainer_email='ops@sightmachine.com',
      zip_safe=False,
      packages=find_packages("python-package"),
      include_package_data=True,
      ext_modules=[shared_lib],
      package_dir={'': 'python-package'},
      url='https://github.com/Microsoft/LightGBM',
)
