# Copyright (c) [2024-2025] []
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
import numpy as np
import plotly.graph_objs as go
import pytest

import grogupy
from grogupy.viz import plot_pairs


def test_plot_pairs():
    infile = "/Users/danielpozsar/Downloads/nojij/Fe3GeTe2/monolayer/soc/lat3_791/Fe3GeTe2.fdf"
    Fe3GeTe2 = grogupy.Builder(
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), matlabmode=True
    )
    Fe3GeTe2_kspace = grogupy.KSpace()
    Fe3GeTe2_contour = grogupy.Contour(100, 1000, emin=None, eigfile=infile)
    Fe3GeTe2_hamiltonian = grogupy.Hamiltonian(infile, np.array([0, 0, 1]))

    Fe3GeTe2.add_kspace(Fe3GeTe2_kspace)
    Fe3GeTe2.add_contour(Fe3GeTe2_contour)
    Fe3GeTe2.add_hamiltonian(Fe3GeTe2_hamiltonian)
    Fe3GeTe2.setup_from_range(20, [[3, 4, 5], [3, 4, 5]])

    fig = plot_pairs(Fe3GeTe2.pairs)

    assert isinstance(fig, go.Figure)
