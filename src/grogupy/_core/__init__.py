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
Core
====

.. currentmodule:: grogupy.batch

This subpackage contains routines to automatically set up and run convergence
 tests and time the calculations.

Core functions
--------------

It contains the core functions of the calculation. There are mathematical functions, 
``Contour``, ``Kspace`` and ``Hamiltonian`` methods, magnetic entity and pair generation.


.. autosummary::
   :toctree: _generated/

   DefaultTimer                 This class measures and stores the runtime of each object.


Constants
---------

Here are the physical constants and default values for the input.

Cpu solvers
-----------

Functions used in the solution method of the ``Builder`` class.

.. autosummary::
   :toctree: _generated/

   solve_parallel_over_k        It calculates the energies by the Greens function method.


Gpu solvers
-----------

Functions used in the solution method of the ``Builder`` class.

.. autosummary::
   :toctree: _generated/

   solve_parallel_over_k        It calculates the energies by the Greens function method.
   gpu_solver                   Parallelizes the Green's function solution on GPU.

Utilities
---------

Miscellaneous functions used around the code...

.. autosummary::
   :toctree: _generated/


"""
