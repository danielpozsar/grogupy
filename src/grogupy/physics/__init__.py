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
Physics
=======

.. currentmodule:: grogupy.physics

This subpackage contains the physical classes and functions closely related 
to energy and magnetic parameter calculation.


Physical classes
----------------

.. autosummary::
   :toctree: _generated/

   Builder                 The main class that holds together the whole simulation.
   Contour                 Energy contour integral.
   Hamiltonian             The Hamiltonian describing the DFT part and useful methods.
   Kspace                  Brillouin zone integral.
   MagneticEntity          Magnetic entity containing useful methods and information.
   Pair                    Pair built from two magnetic entities and a supercell shift.
   PairList                List of Pairs.
   MagneticEntityList      List of MagneticEntities.

Background information
----------------------

This module contains the high level API of the package. It was purposefully 
written to be highly modular, which is ideal for complicated systems that are 
easier to set up and develop in a jupyter notebook environment. 
"""

from .._core.physics_utilities import *
from .builder import *
from .contour import *
from .hamiltonian import *
from .kspace import *
from .magnetic_entity import *
from .pair import *
