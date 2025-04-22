# Copyright (c) [2024-2025] [Laszlo Oroszlany, Daniel Pozsar]
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
from the ``grogupy`` package.

Input/Output Functions
----------------------

.. autosummary::
   :toctree: _generated/

   load_DefaultTimer
   load_Contour
   load_Kspace
   load_MagneticEntity
   load_Pair
   load_Hamiltonian
   load_Builder
   load                     General loader for any grogupy instance.
   save                     Saves instances in a pickled dictionary.
   read_magnopy
   save_magnopy             Saves instances in magnopy input format.
   read_fdf

Utility functions
-----------------

.. autosummary::
   :toctree: _generated/

   decipher
   decipher_all_by_pos
   decipher_all_by_tag
   strip_dict_structure

Background information
----------------------

These functions were written early in the developement and a lot changed since
then. The functions are not used in the main code and are not tested. They are
here for reference and for future development, but they should be rewritten.

Examples
--------

For examples, see the various functions.

"""

from .io import *
from .utilities import *
