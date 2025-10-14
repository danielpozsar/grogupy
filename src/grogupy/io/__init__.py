# Copyright (c) [2024-2025] [Grogupy Team]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Input/Output
=============

.. currentmodule:: grogupy.io

This subpackage contains various routines to read in different input files
and to process the information. The main goal is to convert the information
from the input files to a format that can be used by the ``Builder`` class 
and to save the data in input formats supported by other software.

Input/Output Functions
----------------------

These are the main input output functions for the user.

.. autosummary::
   :toctree: _generated/

   load                         General loader for any grogupy instance from the pickled dictionary.
   save                         General saver  for any grogupy instance, it stores the data in a pickled dictionary.
   save_grogupy                 Creates a .txt file, that contains all the information from a calculated Builder.
   read_grogupy                 Reads a .grogupy.txt file and rebuilds a Builder instance.
   save_magnopy                 Creates a magnopy input file from a calculated Builder.
   save_UppASD                  Creates the UppASD Atomistic Spin Dinamics input file from a calculated Builder.
   save_Vampire                 Creates the Vampire input files from a calculated Builder.
   save_HDF5                    Creates a HDF5 file from a calculated Builder.
   read_fdf                     Reads input for command line tools from an fdf file.
   read_py                      Reads input for command line tools from a python file.

"""

from .._core.io_utilities import *
from .io import *
