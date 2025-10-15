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
.. currentmodule:: grogupy

tqdm in grogupy
---------------

tqdm is optional in grogupy, but when it is in use grogupy uses its own wrapper 
to handle edge cases and print only on the root node, when there is MPI 
parallelization.


.. autosummary::
   :toctree: _generated/

    _tqdm   Tqdm wrapper module for grogupy.

Configuration
-------------
This module contains the configuration from the environment, which helps to 
load or avoid the optional dependencies that can be part of grogupy. These 
optional dependencies are tqdm, CuPy for gpu acceleration and Plotly for 
visualization.


.. autosummary::
   :toctree: _generated/

   Config   Class holding the configuration from the environment.

The ``CONFIG`` instance contains the configuration of grogupy.

"""

__all__ = []
__version__ = "0.3.1"
version = __version__

# this is for version numbering
from sisl import __version__ as __sisl__version__

from .config import *

# pre-import stuff
from .io import (
    load,
    read_grogupy,
    save,
    save_grogupy,
    save_HDF5,
    save_magnopy,
    save_UppASD,
    save_Vampire,
)
from .physics import (
    Builder,
    Contour,
    Hamiltonian,
    Kspace,
    MagneticEntity,
    MagneticEntityList,
    Pair,
    PairList,
)

# extend namespace
__all__.extend(
    [
        "save",
        "save_grogupy",
        "read_grogupy",
        "save_magnopy",
        "save_UppASD",
        "save_Vampire",
        "save_HDF5",
        "load",
        "Contour",
        "Kspace",
        "MagneticEntity",
        "MagneticEntityList",
        "Pair",
        "PairList",
        "Hamiltonian",
        "Builder",
    ]
)


__bibtex__ = r"""
@article{martinez2023relativistic,
    title={Relativistic magnetic interactions from nonorthogonal basis sets},
    author={Mart{\'\i}nez-Carracedo, Gabriel and Oroszl{\'a}ny, L{\'a}szl{\'o} and Garc{\'\i}a-Fuente, Amador and Ny{\'a}ri, Bendeg{\'u}z and Udvardi, L{\'a}szl{\'o} and Szunyogh, L{\'a}szl{\'o} and Ferrer, Jaime},
    journal={Physical Review B},
    volume={108},
    number={21},
    pages={214418},
    year={2023},
    publisher={APS}
}

@software{zerothi_grogupy,
    author={D{\'a}niel Tibor, Pozs{\'a}r and Gabriel, Mart{\'\i}nez-Carracedo and Amador, Garc{\'\i}a-Fuente and L{\'a}szl{\'o}, Udvardi and L{\'a}szl{\'o}, Szunyogh and L{\'a}szl{\'o}, Oroszl{\'a}ny and Jaime, Ferrer},
    title={grogupy: v%s},
    year={2024-2025},
    doi={10.5281/zenodo.15449541},
    url={https://doi.org/10.5281/zenodo.15449541}
}

@software{zerothi_sisl,
author={Papior, Nick},
title={sisl: v%s},
year={2024},
doi={10.5281/zenodo.597181},
url={https://doi.org/10.5281/zenodo.597181}
}

""" % (
    __version__,
    __sisl__version__,
)


__citation__ = __bibtex__
cite = __bibtex__

__definitely_not_grogu__ = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡶⠶⠶⢶⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⢀⣠⣴⡶⠟⠛⠉⠉⠉⠉⠙⠛⠻⠶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣷⣄⠀⠐⠢⠤⣈⡉⠉⠛⠛⠳⠶⢶⡾⠛⠉⠁⠀⣀⠀⠀⠀⡀⠀⠀⢀⠀⠀⠀⠉⠻⢶⣤⣤⣴⣶⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⣶⡀
⠀⠀⠙⢷⣄⠀⠀⠀⠉⠓⠲⢦⣄⡀⠀⠀⠀⠀⠀⠀⠈⠑⣄⠀⣧⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⠤⠤⠄⠂⠀⠀⣠⡿⠁
⠀⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠙⣿⡄⣠⣖⣿⣿⣯⣳⣄⠈⠁⠀⠀⠁⢠⣾⣿⣿⣷⣦⠀⠀⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀
⠀⠀⠀⠀⠀⠻⣦⡀⠀⠀⠀⠀⠀⢸⡏⢹⣿⣿⣿⣿⣿⣧⠀⣠⡤⣀⢀⣾⣿⣿⣿⣿⣿⠃⠸⡏⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⣦⣄⡀⠀⠀⠀⢧⠀⠙⠿⠿⠿⠿⠛⠀⠓⠒⠊⠈⠻⠿⠿⠿⠛⠁⠀⣸⠀⠀⠀⠀⠀⣀⣤⡾⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠶⣶⣾⣧⡀⠀⠀⢀⣀⡀⠐⠒⠒⠒⡤⡀⣀⣀⣀⣠⣤⣾⢷⣶⣶⡾⠟⠛⠉⠁⠀          ██████╗   ██████╗   ██████╗   ██████╗  ██╗   ██╗ ██████╗  ██╗   ██╗
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠈⠛⠋⠙⠛⢩⠿⠛⠛⠋⠉⠉⠉⠉⠉⠀⠀⠀⣠⣼⠿⠻⣿⡆⠀⠀⠀⠀          ██╔════╝  ██╔══██╗ ██╔═══██╗ ██╔════╝  ██║   ██║ ██╔══██╗ ╚██╗ ██╔╝
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣷⣄⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠞⣿⠛⠀⠈⣹⣷⠀⠀⠀⠀          ██║  ███╗ ██████╔╝ ██║   ██║ ██║  ███╗ ██║   ██║ ██████╔╝  ╚████╔╝ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢻⡀⠉⣻⠲⣤⣬⡇⠀⠀⢀⣀⣤⡾⠛⠉⣼⡿⠀⢻⡤⢶⣿⠟⠋⠀⠀⠀⠀          ██║   ██║ ██╔══██╗ ██║   ██║ ██║   ██║ ██║   ██║ ██╔═══╝    ╚██╔╝  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣄⠷⢤⣿⠀⡜⠛⠛⡟⠛⢻⠉⠉⠀⢀⡜⢸⣷⡀⠈⣀⣾⡏⠀⠀⠀⠀⠀⠀          ╚██████╔╝ ██║  ██║ ╚██████╔╝ ╚██████╔╝ ╚██████╔╝ ██║         ██║   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣈⡷⢤⣯⣴⠃⠀⢸⠁⠀⡿⠀⣀⡴⠋⢀⡾⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀             ╚═════╝  ╚═╝  ╚═╝  ╚═════╝   ╚═════╝   ╚═════╝  ╚═╝         ╚═╝
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢻⣿⠉⠀⣠⠄⡟⠀⠀⡇⠀⠉⠀⠀⠺⠃⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡤⠞⠁⠀⡇⠀⠀⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⣷⠀⠀⡇⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠶⠶⠶⠶⠿⠶⠶⠷⠶⠶⠶⠶⠶⠾⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
