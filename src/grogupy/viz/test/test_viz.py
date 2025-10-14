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

from grogupy.io import load_Builder
from grogupy.viz import (
    plot_1D_convergence,
    plot_contour,
    plot_DM_distance,
    plot_DMI,
    plot_J_S_distance,
    plot_Jiso_distance,
    plot_kspace,
    plot_magnetic_entities,
    plot_onsite_anisotropy,
    plot_pairs,
)

pytestmark = [pytest.mark.viz, pytest.mark.need_benchmark_data]


class TestPlots:
    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("marker_size", [1, 10])
    @pytest.mark.parametrize("marker_opacity", [0.1, 0.5])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    @pytest.mark.parametrize("legend", [True, False])
    def test_contour(
        self, path, marker_size, marker_opacity, width, height, title, legend
    ):
        setup = load_Builder(path)
        if setup.contour is not None:
            fig = plot_contour(
                setup.contour,
                marker_size=marker_size,
                marker_opacity=marker_opacity,
                width=width,
                height=height,
                title=title,
                legend=legend,
            )
            assert isinstance(fig, go.Figure)
        else:
            assert False

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("marker_size", [1, 10])
    @pytest.mark.parametrize("marker_opacity", [0.1, 0.5])
    @pytest.mark.parametrize("colorscale", ["Viridis", "Plasma"])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    @pytest.mark.parametrize("legend", [True, False])
    def test_kspace(
        self,
        path,
        marker_size,
        marker_opacity,
        colorscale,
        width,
        height,
        title,
        legend,
    ):
        setup = load_Builder(path)
        if setup.kspace is not None:
            fig = plot_kspace(
                setup.kspace,
                marker_size=marker_size,
                marker_opacity=marker_opacity,
                colorscale=colorscale,
                width=width,
                height=height,
                title=title,
                legend=legend,
            )
            assert isinstance(fig, go.Figure)
        else:
            assert False

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("tags", [None, ["a", "b", "c"]])
    @pytest.mark.parametrize("colors", [None, ["blue", "green", "red"]])
    @pytest.mark.parametrize("marker_size", [1, 10])
    @pytest.mark.parametrize("marker_opacity", [0.1, 0.5])
    @pytest.mark.parametrize("show_cell", [True, False])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    @pytest.mark.parametrize("legend", [True, False])
    def test_magnetic_entities(
        self,
        path,
        tags,
        colors,
        marker_size,
        marker_opacity,
        show_cell,
        width,
        height,
        title,
        legend,
    ):
        setup = load_Builder(path)
        fig = plot_magnetic_entities(
            setup.magnetic_entities[:3],
            tags=tags,
            colors=colors,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            show_cell=show_cell,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )

        assert isinstance(fig, go.Figure)
        fig = plot_magnetic_entities(
            setup,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("colorscale", ["Viridis", "Plasma"])
    @pytest.mark.parametrize("show_cell", [True, False])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    def test_onsite_anisotropy(self, path, colorscale, show_cell, width, height, title):
        setup = load_Builder(path)
        fig = plot_onsite_anisotropy(
            setup.magnetic_entities,
            colorscale=colorscale,
            show_cell=show_cell,
            width=width,
            height=height,
            title=title,
        )
        assert isinstance(fig, go.Figure)
        fig = plot_onsite_anisotropy(
            setup,
            colorscale=colorscale,
            show_cell=show_cell,
            width=width,
            height=height,
            title=title,
        )
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("group", [True, False])
    @pytest.mark.parametrize("connect", [True, False])
    @pytest.mark.parametrize("tags", [None, ["a"]])
    @pytest.mark.parametrize("colors", [None, ["blue", "green"]])
    @pytest.mark.parametrize("marker_size", [1, 10])
    @pytest.mark.parametrize("marker_opacity", [0.1, 0.5])
    @pytest.mark.parametrize("show_cell", [True, False])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    @pytest.mark.parametrize("legend", [True, False])
    def test_pairs(
        self,
        path,
        group,
        connect,
        tags,
        colors,
        marker_size,
        marker_opacity,
        show_cell,
        width,
        height,
        title,
        legend,
    ):
        setup = load_Builder(path)
        fig = plot_pairs(
            setup.pairs[:3],
            group=group,
            connect=connect,
            tags=tags,
            colors=colors,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            show_cell=show_cell,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)
        fig = plot_pairs(
            setup,
            group=group,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            show_cell=show_cell,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("heatplot", [True, False])
    @pytest.mark.parametrize("rescale", [-1, 0, 0.1, 1])
    @pytest.mark.parametrize("tags", [None, ["a", "b", "c"]])
    @pytest.mark.parametrize("colors", [None, ["blue", "green", "red"]])
    @pytest.mark.parametrize("colorscale", ["Viridis", "Plasma"])
    @pytest.mark.parametrize("show_cell", [True, False])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    @pytest.mark.parametrize("legend", [True, False])
    def test_DMI(
        self,
        path,
        heatplot,
        rescale,
        tags,
        colors,
        colorscale,
        show_cell,
        width,
        height,
        title,
        legend,
    ):
        setup = load_Builder(path)
        fig = plot_DMI(
            setup.pairs[:3],
            heatplot=heatplot,
            rescale=rescale,
            tags=tags,
            colors=colors,
            colorscale=colorscale,
            show_cell=show_cell,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)
        fig = plot_DMI(
            setup,
            heatplot=heatplot,
            rescale=rescale,
            colorscale=colorscale,
            show_cell=show_cell,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("group", [True, False])
    @pytest.mark.parametrize("tags", [None, ["a", "b", "c"]])
    @pytest.mark.parametrize("colors", [None, ["blue", "green", "red"]])
    @pytest.mark.parametrize("marker_size", [1, 10])
    @pytest.mark.parametrize("marker_opacity", [0.1, 0.5])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    @pytest.mark.parametrize("legend", [True, False])
    def test_Jiso_distance(
        self,
        path,
        group,
        tags,
        colors,
        marker_size,
        marker_opacity,
        width,
        height,
        title,
        legend,
    ):
        setup = load_Builder(path)
        fig = plot_Jiso_distance(
            setup.pairs[:3],
            group=group,
            tags=tags,
            colors=colors,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )

        assert isinstance(fig, go.Figure)
        fig = plot_Jiso_distance(
            setup,
            group=group,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("group", [True, False])
    @pytest.mark.parametrize("normalise", [True, False])
    @pytest.mark.parametrize("tags", [None, ["a", "b", "c"]])
    @pytest.mark.parametrize("colors", [None, ["blue", "green", "red"]])
    @pytest.mark.parametrize("marker_size", [1, 10])
    @pytest.mark.parametrize("marker_opacity", [0.1, 0.5])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    @pytest.mark.parametrize("legend", [True, False])
    def test_DM_distance(
        self,
        path,
        group,
        normalise,
        tags,
        colors,
        marker_size,
        marker_opacity,
        width,
        height,
        title,
        legend,
    ):
        setup = load_Builder(path)
        fig = plot_DM_distance(
            setup.pairs[:3],
            group=group,
            normalise=normalise,
            tags=tags,
            colors=colors,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)
        fig = plot_DM_distance(
            setup,
            group=group,
            normalise=normalise,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize(
        "path",
        [
            "./benchmarks/test_builder.pkl",
            "./benchmarks/test_builder_2.pkl",
        ],
    )
    @pytest.mark.parametrize("group", [True, False])
    @pytest.mark.parametrize("tags", [None, ["a", "b", "c"]])
    @pytest.mark.parametrize("colors", [None, ["blue", "green", "red"]])
    @pytest.mark.parametrize("marker_size", [1, 10])
    @pytest.mark.parametrize("marker_opacity", [0.1, 0.5])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    @pytest.mark.parametrize("legend", [True, False])
    def test_J_S_distance(
        self,
        path,
        group,
        tags,
        colors,
        marker_size,
        marker_opacity,
        width,
        height,
        title,
        legend,
    ):
        setup = load_Builder(path)
        fig = plot_J_S_distance(
            setup.pairs[:3],
            group=group,
            tags=tags,
            colors=colors,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)
        fig = plot_J_S_distance(
            setup,
            group=group,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            width=width,
            height=height,
            title=title,
            legend=legend,
        )
        assert isinstance(fig, go.Figure)

    @pytest.mark.parametrize("atol", [1e-5, 1, 10])
    @pytest.mark.parametrize("rtol", [1e-5, 1, 10])
    @pytest.mark.parametrize("marker_size", [1, 10])
    @pytest.mark.parametrize("marker_opacity", [0.1, 0.5])
    @pytest.mark.parametrize("width", [500, 1000])
    @pytest.mark.parametrize("height", [500, 1000])
    @pytest.mark.parametrize("title", [None, "title"])
    def test_1D_convergence(
        self,
        atol,
        rtol,
        marker_size,
        marker_opacity,
        width,
        height,
        title,
    ):
        fig = plot_1D_convergence(
            files=["./benchmarks/plot1.pkl", "./benchmarks/plot2.pkl"],
            atol=atol,
            rtol=rtol,
            marker_size=marker_size,
            marker_opacity=marker_opacity,
            width=width,
            height=height,
            title=title,
        )

        assert isinstance(fig, go.Figure)


if __name__ == "__main__":
    pass
