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

import plotly.graph_objs as go
import pytest

import grogupy
from grogupy.viz import *

pytestmark = [pytest.mark.viz, pytest.mark.need_benchmark_data]


class TestPlots:
    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    def test_contour(self, path):
        setup = grogupy.load(path)
        fig = plot_contour(setup.contour)
        assert isinstance(fig, go.Figure)
        fig = plot_contour(setup)
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    def test_kspace(self, path):
        setup = grogupy.load(path)
        fig = plot_kspace(setup.kspace)
        assert isinstance(fig, go.Figure)
        fig = plot_kspace(setup)
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    def test_magnetic_entities(self, path):
        setup = grogupy.load(path)
        fig = plot_magnetic_entities(setup.magnetic_entities)
        assert isinstance(fig, go.Figure)
        fig = plot_magnetic_entities(setup)
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    def test_onsite_anisotropy(self, path):
        setup = grogupy.load(path)
        fig = plot_onsite_anisotropy(setup.magnetic_entities)
        assert isinstance(fig, go.Figure)
        fig = plot_onsite_anisotropy(setup)
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("connect", [True, False])
    @pytest.mark.parametrize("cell", [True, False])
    def test_pairs(self, setup, path, connect, cell):
        setup = grogupy.load(path)
        fig = plot_pairs(setup.pairs, connect, cell)
        assert isinstance(fig, go.Figure)
        fig = plot_pairs(setup, connect, cell)
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("rescale", [-1, 0, 0.1, 1])
    def test_DMI(self, path, rescale):
        setup = grogupy.load(path)
        fig = plot_DMI(setup.pairs, rescale)
        assert isinstance(fig, go.Figure)
        fig = plot_DMI(setup, rescale)
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("normalise", [True, False])
    @pytest.mark.parametrize("group", [True, False])
    def test_DM_distance(self, normalise, group):
        setup = grogupy.load(path)
        fig = plot_DM_distance(setup.pairs, normalise, group)
        assert isinstance(fig, go.Figure)
        fig = plot_DM_distance(setup, normalise, group)
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("group", [True, False])
    def test_Jiso_distance(self, path, group):
        setup = grogupy.load(path)
        fig = plot_Jiso_distance(setup.pairs, group)
        assert isinstance(fig, go.Figure)
        fig = plot_Jiso_distance(setup, group)
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("group", [True, False])
    def test_J_S_distance(self, path, group):
        setup = grogupy.load(path)
        fig = plot_J_S_distance(setup.pairs, group)
        assert isinstance(fig, go.Figure)
        fig = plot_J_S_distance(setup, group)
        assert isinstance(fig, go.Figure)

    @pytest.mark.xfail(raises=NotImplementedError)
    @pytest.mark.parametrize("files", [True, False])
    @pytest.mark.parametrize("parameter", ["eset", "esetp", "kset"])
    @pytest.mark.parametrize("maxdiff", [-1, 0, 100, 1e-5])
    @pytest.mark.parametrize("method", ["absolute", "relative"])
    def test_1D_convergence(self, files, parameter, maxdiff, method):
        fig = plot_1D_convergence(files, parameter, maxdiff, method)
        assert isinstance(fig, go.Figure)


if __name__ == "__main__":
    pass
