# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2018 by Lars Klitzke, Lars.Klitzke@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import setuptools

# read in the long description written in the README.rst file
with open("README.rst", "r") as fh:
    long_description = fh.read()

__version__ = '0.0.2'

setuptools.setup(
    name='pymodconf',
    version=__version__,
    description='Modularized configuration files.',
    long_description=long_description,
    author='Lars Klitzke',
    author_email='Lars.Klitzke@gmail.com',
    classifiers=(
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Natural Language :: English",
    ),
    packages=setuptools.find_packages()
)
