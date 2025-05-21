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

infolder = "./benchmarks/Cr3"
infile = "Cr3.fdf"
################################################################################
#                            Convergence parameters
################################################################################
# kset should be at leas 100x100 for 2D diatomic systems
kset = [1, 1, 1]
# eset should be 100 for insulators and 1000 for metals
eset = 100
# esetp should be 600 for insulators and 10000 for metals
esetp = 600
# emin None sets the minimum energy to the minimum energy in the eigfile
emin = -100
# emax is at the Fermi level at 0
emax = 0
# the bottom of the energy contour should be shifted by -5 eV
emin_shift = -5
# the top of the energy contour can be shifted to the middle of the gap for
# insulators
emax_shift = 0
################################################################################
#                                 Orientations
################################################################################
# usually the DFT calculation axis is [0, 0, 1]
scf_xcf_orientation = [0, 0, 1]
# the reference directions for the energy derivations
ref_xcf_orientations = [
    dict(o=[1, 0, 0], vw=[[0, 1, 0], [0, 0, 1]]),
    dict(o=[0, 1, 0], vw=[[1, 0, 0], [0, 0, 1]]),
    dict(o=[0, 0, 1], vw=[[1, 0, 0], [0, 1, 0]]),
]
################################################################################
#                      Magnetic entity and pair definitions
################################################################################
# magnetic entities and pairs can be defined automatically from the cutoff
# radius and magnetic atoms
setup_from_range = False


radius = 20
atomic_subset = "Cr"
kwargs_for_mag_ent = dict(l=2)
magnetic_entities = [
    dict(atom=0, l=2),
    dict(atom=1, l=2),
    dict(atom=2, l=2),
]
pairs = [
    dict(ai=0, aj=1, Ruc=[0, 0, 0]),
    dict(ai=1, aj=2, Ruc=[0, 0, 0]),
    dict(ai=2, aj=0, Ruc=[0, 0, 0]),
]
################################################################################
#                                Memory management
################################################################################
# maximum number of pairs per loop, reduce it to avoid memory overflow
max_pairs_per_loop = 100
# in low memory mode we discard some temporary data that could be useful for
# interactive work
low_memory_mode = True
# sequential solver is better for large systems
greens_function_solver = "Parallel"
# maximum number of greens function samples per loop, when greens_function_solver
# is set to "Sequential", reduce it to avoid memory overflow on GPU for large
# systems
max_g_per_loop = 20
################################################################################
#                                 Solution methods
################################################################################
# the calculation of J and K from the energy derivations, either Fit or Grogupy
spin_model = "generalised-fit"
################################################################################
#                                   Output files
################################################################################
# either total or local, which controls if only the magnetic
# entity's magnetic monent or the whole atom's magnetic moment is printed
# used by all output modes
out_magnetic_moment = "local"

# save the magnopy file
save_magnopy = True
# precision of numerical values in the magnopy file
magnopy_precision = None
# add the simulation parameters to the magnopy file as comments
magnopy_comments = True

# save the Uppsala Atomistic Spin Dynamics software input files
# uses the outfolder and out_magentic_moment
save_UppASD = True

# save the pickle file
save_pickle = True
"""
The compression level can be set to 0,1,2,3. Every other value defaults to 3.
0. This means that there is no compression at all.

1. This means, that the keys "_dh" and "_ds" are set
   to None, because othervise the loading would be dependent
   on the sisl version

2. This contains compression 1, but sets the keys "Gii",
   "Gij", "Gji", "Vu1" and "Vu2" to [], to save space
"""
pickle_compress_level = 10

# output folder, for example the current folder
outfolder = "./src/grogupy/cli/tests/"
# outfile name
outfile = "test"
################################################################################
################################################################################
