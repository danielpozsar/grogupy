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

from typing import Union

import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import sisl
from numpy.typing import NDArray

from grogupy.io import load_Builder
from grogupy.physics import (
    Builder,
    Contour,
    Kspace,
    MagneticEntity,
    MagneticEntityList,
    Pair,
    PairList,
)


def _plot_cell(fig: go.Figure, cell: NDArray) -> go.Figure:
    """Add unit cell to figure.

    Parameters
    ----------
    fig : go.Figure
        Plotly figure without the cell
    cell : NDArray
        Unit cell matrix

    Returns
    -------
    go.Figure
        Figure containing the cell
    """
    a1 = cell[0, :]
    a2 = cell[1, :]
    a3 = cell[2, :]
    vecs0 = np.array(
        [
            np.zeros(3),
            np.zeros(3),
            np.zeros(3),
            a1,
            a1,
            a2,
            a2,
            a3,
            a3,
            a1 + a2 + a3,
            a1 + a2 + a3,
            a1 + a2 + a3,
        ]
    )
    vecs1 = np.array(
        [
            a1,
            a2,
            a3,
            a1 + a2,
            a1 + a3,
            a2 + a1,
            a2 + a3,
            a3 + a1,
            a3 + a2,
            a1 + a2,
            a1 + a3,
            a2 + a3,
        ]
    )
    for v1, v2 in zip(vecs0, vecs1):
        fig.add_trace(
            go.Scatter3d(
                x=[v1[0], v2[0]],
                y=[v1[1], v2[1]],
                z=[v1[2], v2[2]],
                mode="lines",
                showlegend=False,
                line=dict(color="black", width=1),
            )
        )
    return fig


def plot_contour(
    contour: Contour,
    marker_size: float = 10,
    marker_opacity: float = 1,
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
    legend: bool = True,
) -> go.Figure:
    """Creates a plot from the contour sample points.

    If there are too many eigenvalues, then they are subsamled
    for the plot.

    Parameters
    ----------
    contour : Contour
        Contour class that contains the energy samples and weights
    marker_size : float, optional
        Size of the markers, by default 10
    marker_opacity : float, optional
        Opacity of the markers, by default 1
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None
    legend : bool, optional
        Whether to show the legend, by default True

    Returns
    -------
    plotly.graph_objs.go.Figure
        The created figure
    """

    # Create the scatter plot
    trace = go.Scatter(
        x=contour.samples.real,
        y=contour.samples.imag,
        mode="markers",
        name="Contour points",
        marker=dict(
            size=marker_size,
            opacity=marker_opacity,
        ),
    )

    # if the eigenvalues are available
    if contour.automatic_emin:
        # convert the path to the EIG file
        eigfile = contour._eigfile
        if eigfile.endswith("fdf"):
            eigfile = eigfile[:-3] + "EIG"

        # try to use the path to the EIG file...
        try:
            # read eigenvals
            eigs = sisl.get_sile(eigfile).read_data().flatten()
            eigs.sort()
            # if there are too many eigenvalues subsample them for the plot
            if len(eigs) > 10000:
                eigs = eigs[:: int(len(eigs) / 10000)]
                # traces to eigenvals
                eig_trace1 = go.Scatter(
                    x=eigs[eigs < 0],
                    y=np.zeros_like(eigs[eigs < 0]),
                    mode="markers",
                    name="Subsampled occupied DFT eigs",
                    marker=dict(
                        size=marker_size,
                        opacity=marker_opacity,
                    ),
                )
                eig_trace2 = go.Scatter(
                    x=eigs[0 < eigs],
                    y=np.zeros_like(eigs[0 < eigs]),
                    mode="markers",
                    name="Subsampled unoccupied DFT eigs",
                    marker=dict(
                        size=marker_size,
                        opacity=marker_opacity,
                    ),
                )
            else:
                eig_trace1 = go.Scatter(
                    x=eigs[eigs < 0],
                    y=np.zeros_like(eigs[eigs < 0]),
                    mode="markers",
                    name="Occupied DFT eigs",
                    marker=dict(
                        size=marker_size,
                        opacity=marker_opacity,
                    ),
                )
                eig_trace2 = go.Scatter(
                    x=eigs[0 < eigs],
                    y=np.zeros_like(eigs[0 < eigs]),
                    mode="markers",
                    name="Unoccupied DFT eigs",
                    marker=dict(
                        size=marker_size,
                        opacity=marker_opacity,
                    ),
                )
            fig = go.Figure(data=[trace, eig_trace1, eig_trace2])
        # but something might have been moved, in which case just do the regular plot
        except:
            fig = go.Figure(data=trace)

    # else just plot the contour
    else:
        fig = go.Figure(data=trace)

    # Update the layout
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        title=title,
        xaxis_title="Real axis [eV]",
        yaxis_title="Imaginary axis [eV]",
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
        ),
        legend=dict(
            x=1,
            y=1,
            xanchor="right",
        ),
        showlegend=legend,
    )

    return fig


def plot_kspace(
    kspace: Kspace,
    marker_size: float = 10,
    marker_opacity: float = 1,
    colorscale: str = "Viridis",
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
    legend: bool = True,
) -> go.Figure:
    """Creates a plot from the Brillouin zone sample points.

    Parameters
    ----------
    kspace : Kspace
        Kspace class that contains the Brillouin-zone samples and weights
    colorscale : str, optional
        The colorscale of the weights, by default Viridis
    marker_size : float, optional
        Size of the markers, by default 10
    marker_opacity : float, optional
        Opacity of the markers, by default 1
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None
    legend : bool, optional
        Whether to show the legend, by default True

    Returns
    -------
    plotly.graph_objs.go.Figure
        The created figure
    """

    # Create the scatter plot
    # Create 3D scatter plot
    trace = go.Scatter3d(
        name=f"Kpoints",
        x=kspace.kpoints[:, 0],
        y=kspace.kpoints[:, 1],
        z=kspace.kpoints[:, 2],
        mode="markers",
        marker=dict(
            size=marker_size,
            color=kspace.weights,
            colorscale=colorscale,
            opacity=marker_opacity,
            colorbar=dict(title="Weights of kpoints", x=0.75),
        ),
    )

    # Update the layout

    layout = go.Layout(
        autosize=False,
        title=title,
        width=width,
        height=height,
        scene=dict(
            aspectmode="data",
            xaxis=dict(title="X Axis", showgrid=True, gridwidth=1),
            yaxis=dict(title="Y Axis", showgrid=True, gridwidth=1),
            zaxis=dict(title="Z Axis", showgrid=True, gridwidth=1),
        ),
        showlegend=legend,
    )

    # Create figure and show
    fig = go.Figure(data=[trace], layout=layout)

    return fig


def plot_magnetic_entities(
    magnetic_entities: Union[Builder, list[MagneticEntity], MagneticEntityList],
    tags: Union[None, list[str]] = None,
    colors: Union[None, list[str]] = None,
    marker_size: float = 5,
    marker_opacity: float = 1,
    show_cell: bool = True,
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
    legend: bool = True,
) -> go.Figure:
    """Creates a plot from a list of magnetic entities.

    Parameters
    ----------
    magnetic_entities : Union[Builder, list[MagneticEntity], MagneticEntityList]
        The magnetic entities that contain the tags and coordinates
    tags : Union[None, list[str]], optional
        The tags of the markers, if None, then it is autogenerated,
        by default None
    colors: Union[None, list[str]], optional
        The colors of the markers, if None, then it is autogenerated,
        by default None
    marker_size : float, optional
        Size of the markers, by default 10
    marker_opacity : float, optional
        Opacity of the markers, by default 1
    show_cell : bool, optional
        Whether to show the cell or not, by default True
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None
    legend : bool, optional
        Whether to show the legend, by default True

    Returns
    -------
    plotly.graph_objs.go.Figure
        The created figure
    """

    # conversion line for the case when it is set as the plot function of a builder
    if isinstance(magnetic_entities, Builder):
        magnetic_entities = magnetic_entities.magnetic_entities
    else:
        magnetic_entities = MagneticEntityList(magnetic_entities)

    if tags is None:
        tags = magnetic_entities.tag
    coords = magnetic_entities._xyz

    if colors is None:
        colors = px.colors.qualitative.D3
        colors = colors * (len(tags) // len(colors) + 1)

    # Create figure
    fig = go.Figure()
    for coord, color, tag in zip(coords, colors, tags):
        fig.add_trace(
            go.Scatter3d(
                name=tag,
                x=coord[:, 0],
                y=coord[:, 1],
                z=coord[:, 2],
                mode="markers",
                marker=dict(size=marker_size, opacity=marker_opacity, color=color),
            )
        )

    # optionally add cell
    if show_cell:
        fig = _plot_cell(fig, magnetic_entities[0].cell)

    # Create layout
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        title=title,
        scene=dict(
            aspectmode="data",
            xaxis=dict(title="X Axis", showgrid=True, gridwidth=1),
            yaxis=dict(title="Y Axis", showgrid=True, gridwidth=1),
            zaxis=dict(title="Z Axis", showgrid=True, gridwidth=1),
        ),
        showlegend=legend,
    )

    return fig


def plot_onsite_anisotropy(
    magnetic_entities: Union[Builder, list[MagneticEntity], MagneticEntityList],
    colorscale: str = "Viridis",
    show_cell: bool = True,
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
) -> go.Figure:
    """Creates a plot of the on-site anisotropy from a list of magnetic entities.

    Based on the work of Marcell Sipos.

    Parameters
    ----------
    magnetic_entities : Union[Builder, list[MagneticEntity], MagneticEntityList]
        The magnetic entities that contain the tags and coordinates
    colorscale : str, optional
        The colorscale of the weights, by default Viridis
    show_cell : bool, optional
        Whether to show the cell or not, by default True
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None
    legend : bool, optional
        Whether to show the legend, by default True

    Returns
    -------
    plotly.graph_objs.go.Figure
        The created figure
    """

    # conversion line for the case when it is set as the plot function of a builder
    if isinstance(magnetic_entities, Builder):
        magnetic_entities = magnetic_entities.magnetic_entities
    else:
        magnetic_entities = MagneticEntityList(magnetic_entities)

    # Create figure
    fig = go.Figure()

    # Create angular grid for unit sphere
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)
    phi_grid, theta_grid = np.meshgrid(phi, theta)

    # Convert spherical to cartesian
    x = np.sin(theta_grid) * np.cos(phi_grid)
    y = np.sin(theta_grid) * np.sin(phi_grid)
    z = np.cos(theta_grid)

    anisotropy_energy = np.zeros((len(magnetic_entities), x.shape[0], x.shape[1]))
    for m, mag_ent in enumerate(magnetic_entities):
        if mag_ent.K is None:
            raise Exception("On-site anisotropy is not calculated yet!")
        for i in range(100):
            for j in range(100):
                # Unit vector at this point
                S = np.array([x[i, j], y[i, j], z[i, j]])
                # Anisotropy energy
                anisotropy_energy[m, i, j] = S @ mag_ent.K_meV @ S

    # Add surface plot
    for i, m in enumerate(anisotropy_energy):
        if i == 0:
            fig.add_trace(
                go.Surface(
                    x=x + magnetic_entities[i].xyz_center[0],
                    y=y + magnetic_entities[i].xyz_center[1],
                    z=z + magnetic_entities[i].xyz_center[2],
                    surfacecolor=m,
                    colorbar=dict(title="Anisotropy energy [meV]"),
                    colorscale=colorscale,
                    opacity=1,
                    cmin=anisotropy_energy.min(),
                    cmax=anisotropy_energy.max(),
                )
            )
        else:
            fig.add_trace(
                go.Surface(
                    x=x + magnetic_entities[i].xyz_center[0],
                    y=y + magnetic_entities[i].xyz_center[1],
                    z=z + magnetic_entities[i].xyz_center[2],
                    surfacecolor=m,
                    colorscale=colorscale,
                    opacity=1,
                    showscale=False,
                )
            )

    # optionally add cell
    if show_cell:
        fig = _plot_cell(fig, magnetic_entities[0].cell)

    # Create layout
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        title=title,
        scene=dict(
            aspectmode="data",
            xaxis=dict(title="X Axis", showgrid=True, gridwidth=1),
            yaxis=dict(title="Y Axis", showgrid=True, gridwidth=1),
            zaxis=dict(title="Z Axis", showgrid=True, gridwidth=1),
        ),
    )

    return fig


def plot_pairs(
    pairs: Union[Builder, list[Pair], PairList],
    group: bool = True,
    tags: Union[None, list[str]] = None,
    colors: Union[None, list[str]] = None,
    marker_size: float = 10,
    marker_opacity: float = 0.5,
    show_cell: bool = True,
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
    legend: bool = True,
) -> go.Figure:
    """Creates a plot from a list of pairs.

    Parameters
    ----------
    pairs : Union[Builder, list[Pair], PairList]
        The pairs that contain the tags and coordinates
    group : bool, optional
        Whether to group the pairs by their first magnetic entity,
        by default True
    tags : Union[None, list[str]], optional
        The tags of the markers, if None, then it is autogenerated,
        by default None
    colors: Union[None, list[str]], optional
        The colors of the markers, if None, then it is autogenerated,
        by default None
    marker_size : float, optional
        Size of the markers, by default 10
    marker_opacity : float, optional
        Opacity of the markers, by default 1
    show_cell : bool, optional
        Whether to show the cell or not, by default True
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None
    legend : bool, optional
        Whether to show the legend, by default True

    Returns
    -------
    plotly.graph_objs.go.Figure
        The created figure
    """

    # conversion line for the case when it is set as the plot function of a builder
    if isinstance(pairs, Builder):
        pairs = pairs.pairs
    else:
        pairs = PairList(pairs)

    # center tags
    ctags = pairs.tags[:, 0]

    ctags, mask = np.unique(ctags, return_inverse=True)

    if tags is not None:
        # setup interacting tags by finding the ctags and changing them
        itags = np.zeros_like(pairs.tags[:, 0], dtype=str)
        for i in range(len(ctags)):
            itags[np.where(pairs.tags[:, 1] == ctags[i])[0]] = tags[i]
        itags = (
            itags
            + ", ruc:"
            + np.apply_along_axis(
                lambda s: f"[{s[0]:d}, {s[1]:d}, {s[2]:d}]", 1, pairs.supercell_shift
            )
        )
        ctags = tags
    else:
        # interacting tags
        itags = (
            pairs.tags[:, 1]
            + ", ruc:"
            + np.apply_along_axis(
                lambda s: f"[{s[0]:d}, {s[1]:d}, {s[2]:d}]", 1, pairs.supercell_shift
            )
        )

    if colors is None:
        colors = px.colors.qualitative.D3
        colors = colors * (len(ctags) // len(colors) + 1)

    # Create figure
    fig = go.Figure()
    for i in range(len(ctags)):
        # center xyz
        cxyz = pairs[mask == i][0].xyz[0]
        # Create 3D scatter plot
        fig.add_trace(
            go.Scatter3d(
                name="Center:" + ctags[i],
                x=cxyz[:, 0],
                y=cxyz[:, 1],
                z=cxyz[:, 2],
                mode="markers",
                marker=dict(size=marker_size, opacity=marker_opacity, color=colors[i]),
            )
        )
        # group to magnetic entities
        if group:
            # interacting xyz
            ixyz = pairs.xyz[mask == i, 1].reshape(-1, 3)
            fig.add_trace(
                go.Scatter3d(
                    name="Pairs on: " + ctags[i],
                    x=ixyz[:, 0],
                    y=ixyz[:, 1],
                    z=ixyz[:, 2],
                    mode="markers",
                    marker=dict(
                        size=marker_size / 2, opacity=marker_opacity, color=colors[i]
                    ),
                )
            )
        # plot separately
        else:
            for j in range(len(pairs[mask == i])):
                legend_group = f"pair {ctags[i]}-{itags[mask == i][j]}"
                # interacting xyz
                ixyz = pairs.xyz[mask == i][j, 1]
                fig.add_trace(
                    go.Scatter3d(
                        name=itags[mask == i][j],
                        x=ixyz[:, 0],
                        y=ixyz[:, 1],
                        z=ixyz[:, 2],
                        legendgroup=legend_group,
                        mode="markers",
                        marker=dict(
                            size=marker_size / 2,
                            opacity=marker_opacity,
                            color=colors[i],
                        ),
                    )
                )

    # optionally add cell
    if show_cell:
        fig = _plot_cell(fig, pairs[0].cell)

    # Create layout
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        title=title,
        scene=dict(
            aspectmode="data",
            xaxis=dict(title="X Axis", showgrid=True, gridwidth=1),
            yaxis=dict(title="Y Axis", showgrid=True, gridwidth=1),
            zaxis=dict(title="Z Axis", showgrid=True, gridwidth=1),
        ),
        showlegend=legend,
    )

    return fig


def plot_DMI(
    pairs: Union[Builder, list[Pair], PairList],
    heatplot: bool = False,
    rescale: float = 1,
    tags: Union[None, list[str]] = None,
    colors: Union[None, list[str]] = None,
    colorscale: str = "Viridis",
    show_cell: bool = True,
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
    legend: bool = True,
) -> go.Figure:
    """Creates a plot of the DM vectors from a list of pairs.

    It can only use pairs from a finished simulation. The magnitude of
    the vectors are in meV. WARNING: because the sizes of the cones are
    also dependent on the norm of the DM vectors, very small DMs can be
    missing from the fgure.

    Parameters
    ----------
    pairs : Union[Builder, list[Pair], PairList]
        The pairs that contain the tags, coordinates and the DM vectors
    heatplot : bool, optional
        Whether to use heatplot or plot all DMs separatly, by default
        False
    rescale : float, optional
        Rescale parameter for the lengths of DM vectors. If this is
        not set to 1, then the lengths are not in meV, by default 1
    tags : Union[None, list[str]], optional
        The tags of the markers, if None, then it is autogenerated,
        by default None
    colors: Union[None, list[str]], optional
        The colors of the markers, if None, then it is autogenerated,
        by default None
    colorscale : str, optional
        The colorscale of the weights, by default Viridis
    show_cell : bool, optional
        Whether to show the cell or not, by default True
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None
    legend : bool, optional
        Whether to show the legend, by default True

    Returns
    -------
    plotly.graph_objs.go.Figure
        The created figure
    """

    # conversion line for the case when it is set as the plot function of a builder
    if isinstance(pairs, Builder):
        pairs = pairs.pairs
    else:
        pairs = PairList(pairs)

    # Define some example vectors
    dms = pairs.D_meV
    if not heatplot:
        dms = dms * rescale

    # Define origins
    origins = pairs.xyz_center.mean(axis=1)

    if tags is None:
        tags = ["-->".join(p.tags) + ", ruc:" + str(p.supercell_shift) for p in pairs]

    if colors is None:
        colors = px.colors.qualitative.D3
        colors = colors * (len(dms) // len(colors) + 1)

    # Create figure
    fig = go.Figure()
    if heatplot:
        # Visualize field with cones
        if rescale == 1:
            ctitle = "DM norm [meV]"
        else:
            ctitle = "Scaled DM norm [ ]"
        fig.add_trace(
            go.Cone(
                x=origins[:, 0],
                y=origins[:, 1],
                z=origins[:, 2],
                u=dms[:, 0],
                v=dms[:, 1],
                w=dms[:, 2],
                colorbar=dict(title=ctitle),
                colorscale=colorscale,
                showscale=True,
            )
        )
    else:
        # Maximum vector magnitude for scaling
        max_magnitude = max(np.linalg.norm(dm) for dm in dms)

        # End point of the vector
        endpoints = origins + dms

        for i in range(len(dms)):
            legend_group = f"vector_{i}"

            # Add a line for the vector
            fig.add_trace(
                go.Scatter3d(
                    x=[origins[i, 0], endpoints[i, 0]],
                    y=[origins[i, 1], endpoints[i, 1]],
                    z=[origins[i, 2], endpoints[i, 2]],
                    mode="lines",
                    line=dict(color=colors[i], width=5),
                    name=tags[i],
                    legendgroup=legend_group,
                    showlegend=True,
                )
            )

            # Add a cone at the end to represent the arrow head
            u, v, w = dms[i]
            fig.add_trace(
                go.Cone(
                    x=[endpoints[i, 0]],
                    y=[endpoints[i, 1]],
                    z=[endpoints[i, 2]],
                    u=[u / 5],  # Scale down for better visualization
                    v=[v / 5],
                    w=[w / 5],
                    colorscale=[[0, colors[i]], [1, colors[i]]],
                    showscale=False,
                    sizemode="absolute",
                    sizeref=max(np.log(max_magnitude), 1),
                    legendgroup=legend_group,
                    showlegend=False,
                )
            )

    # optionally add cell
    if show_cell:
        fig = _plot_cell(fig, pairs[0].cell)

    # Create layout
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        title=title,
        scene=dict(
            aspectmode="data",
            xaxis=dict(title="X Axis", showgrid=True, gridwidth=1),
            yaxis=dict(title="Y Axis", showgrid=True, gridwidth=1),
            zaxis=dict(title="Z Axis", showgrid=True, gridwidth=1),
        ),
        showlegend=legend,
    )

    return fig


def plot_Jiso_distance(
    pairs: Union[Builder, list[Pair], PairList],
    group: bool = False,
    tags: Union[None, list[str]] = None,
    colors: Union[None, list[str]] = None,
    marker_size: float = 10,
    marker_opacity: float = 1,
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
    legend: bool = True,
) -> go.Figure:
    """Plots the isotropic exchange as a function of distance.

    Parameters
    ----------
    pairs : Union[Builder, list[Pair], PairList]
        The pairs that contain the exchange and positions
    group : bool, optional
        Whether to group the pairs by their first magnetic entity,
        by default True
    tags : Union[None, list[str]], optional
        The tags of the markers, if None, then it is autogenerated,
        by default None
    colors: Union[None, list[str]], optional
        The colors of the markers, if None, then it is autogenerated,
        by default None
    marker_size : float, optional
        Size of the markers, by default 10
    marker_opacity : float, optional
        Opacity of the markers, by default 1
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None
    legend : bool, optional
        Whether to show the legend, by default True

    Returns
    -------
    plotly.graph_objs.go.Figure
        The created figure
    """

    # conversion line for the case when it is set as the plot function of a builder
    if isinstance(pairs, Builder):
        pairs = pairs.pairs
    else:
        pairs = PairList(pairs)

    if group:
        _tags = pairs.tags[:, 0] + "-->" + pairs.tags[:, 1]
        _tags, mask = np.unique(_tags, return_inverse=True)
        if tags is None:
            tags = _tags

        values = pairs.J_iso_meV
        dists = pairs.distance
        if colors is None:
            colors = px.colors.qualitative.D3
            colors = colors * (len(tags) // len(colors) + 1)

        # Create figure
        fig = go.Figure()
        for i in range(len(tags)):
            fig.add_trace(
                go.Scatter(
                    name="Jiso: " + tags[i],
                    x=dists[mask == i],
                    y=values[mask == i],
                    mode="markers",
                    marker=dict(
                        size=marker_size, opacity=marker_opacity, color=colors[i]
                    ),
                )
            )
    else:
        if colors is None:
            colors = px.colors.qualitative.D3
        # Create figure
        fig = go.Figure(
            data=go.Scatter(
                x=pairs.distance,
                y=pairs.J_iso_meV,
                mode="markers",
                marker=dict(size=marker_size, opacity=marker_opacity, color=colors[0]),
            )
        )

    # Create layout
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        title=title,
        xaxis_title="Pair distance [Ang]",
        yaxis_title="Isotropic exchange [meV]",
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
        ),
        showlegend=legend,
    )

    return fig


def plot_DM_distance(
    pairs: Union[Builder, list[Pair], PairList],
    group: bool = False,
    normalise: bool = True,
    tags: Union[None, list[str]] = None,
    colors: Union[None, list[str]] = None,
    marker_size: float = 10,
    marker_opacity: float = 1,
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
    legend: bool = True,
) -> go.Figure:
    """Plots the magnitude of DM vectors as a function of distance.

    Parameters
    ----------
    pairs : Union[Builder, list[Pair], PairList]
        The pairs that contain the DM vectors and positions
    group : bool, optional
        Whether to group the pairs by their first magnetic entity,
        by default True
    normalise : bool, optional
        To return the norm of the DM vector or just the elements,
        by default True
    tags : Union[None, list[str]], optional
        The tags of the markers, if None, then it is autogenerated,
        by default None
    colors: Union[None, list[str]], optional
        The colors of the markers, if None, then it is autogenerated,
        by default None
    marker_size : float, optional
        Size of the markers, by default 10
    marker_opacity : float, optional
        Opacity of the markers, by default 1
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None
    legend : bool, optional
        Whether to show the legend, by default True

    Returns
    -------
    plotly.graph_objs.go.Figure
        The created figure
    """

    # conversion line for the case when it is set as the plot function of a builder
    if isinstance(pairs, Builder):
        pairs = pairs.pairs
    else:
        pairs = PairList(pairs)

    if group:
        _tags = pairs.tags[:, 0] + "-->" + pairs.tags[:, 1]
        _tags, mask = np.unique(_tags, return_inverse=True)
        if tags is None:
            tags = _tags

        values = pairs.D_meV
        dists = pairs.distance
        if colors is None:
            colors = px.colors.qualitative.D3
            colors = colors * (len(tags) // len(colors) + 1)

        if normalise:
            # Create figure
            fig = go.Figure()
            for i in range(len(tags)):
                fig.add_trace(
                    go.Scatter(
                        name="DM norm: " + tags[i],
                        x=dists[mask == i],
                        y=np.linalg.norm(values[mask == i], axis=1),
                        mode="markers",
                        marker=dict(
                            size=marker_size, opacity=marker_opacity, color=colors[i]
                        ),
                    )
                )
        else:
            # Create figure
            fig = go.Figure()
            for i in range(len(tags)):
                fig.add_trace(
                    go.Scatter(
                        name="DM_x: " + tags[i],
                        x=dists[mask == i],
                        y=values[mask == i, 0],
                        mode="markers",
                        marker=dict(
                            size=marker_size,
                            opacity=marker_opacity,
                            color=colors[i],
                            symbol="circle-open",
                        ),
                    )
                )
                fig.add_trace(
                    go.Scatter(
                        name="DM_y: " + tags[i],
                        x=dists[mask == i],
                        y=values[mask == i, 1],
                        mode="markers",
                        marker=dict(
                            size=marker_size,
                            opacity=marker_opacity,
                            color=colors[i],
                            symbol="cross",
                        ),
                    )
                )
                fig.add_trace(
                    go.Scatter(
                        name="DM_z: " + tags[i],
                        x=dists[mask == i],
                        y=values[mask == i, 2],
                        mode="markers",
                        marker=dict(
                            size=marker_size,
                            opacity=marker_opacity,
                            color=colors[i],
                            symbol="x",
                        ),
                    )
                )
    else:
        if colors is None:
            colors = px.colors.qualitative.D3
        if normalise:
            # Create figure
            fig = go.Figure(
                data=go.Scatter(
                    name="DM norm",
                    x=pairs.distance,
                    y=np.linalg.norm(pairs.D_meV, axis=1),
                    mode="markers",
                    marker=dict(
                        size=marker_size, opacity=marker_opacity, color=colors[0]
                    ),
                )
            )
        else:
            # Create figure
            fig = go.Figure()
            fig.add_trace(
                go.Scatter(
                    name="DM_x",
                    x=pairs.distance,
                    y=pairs.D_meV[:, 0],
                    mode="markers",
                    marker=dict(
                        size=marker_size, opacity=marker_opacity, color=colors[0]
                    ),
                )
            )
            fig.add_trace(
                go.Scatter(
                    name="DM_y",
                    x=pairs.distance,
                    y=pairs.D_meV[:, 1],
                    mode="markers",
                    marker=dict(
                        size=marker_size, opacity=marker_opacity, color=colors[1]
                    ),
                )
            )
            fig.add_trace(
                go.Scatter(
                    name="DM_z",
                    x=pairs.distance,
                    y=pairs.D_meV[:, 2],
                    mode="markers",
                    marker=dict(
                        size=marker_size, opacity=marker_opacity, color=colors[2]
                    ),
                )
            )

    # Create layout
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        title=title,
        xaxis_title="Pair distance [Ang]",
        yaxis_title="DM vectors [meV]",
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
        ),
        showlegend=legend,
    )

    return fig


def plot_J_S_distance(
    pairs: Union[Builder, list[Pair], PairList],
    group: bool = False,
    tags: Union[None, list[str]] = None,
    colors: Union[None, list[str]] = None,
    marker_size: float = 10,
    marker_opacity: float = 1,
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
    legend: bool = True,
) -> go.Figure:
    """Plots the eigenvalues of symmetric exchange as a function of distance.

    Parameters
    ----------
    pairs : Union[Builder, list[Pair], PairList]
        The pairs that contain the exchange and positions
    group : bool, optional
        Whether to group the pairs by their first magnetic entity,
        by default True
    tags : Union[None, list[str]], optional
        The tags of the markers, if None, then it is autogenerated,
        by default None
    colors: Union[None, list[str]], optional
        The colors of the markers, if None, then it is autogenerated,
        by default None
    marker_size : float, optional
        Size of the markers, by default 10
    marker_opacity : float, optional
        Opacity of the markers, by default 1
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None
    legend : bool, optional
        Whether to show the legend, by default True

    Returns
    -------
    plotly.graph_objs.go.Figure
        The created figure
    """

    # conversion line for the case when it is set as the plot function of a builder
    if isinstance(pairs, Builder):
        pairs = pairs.pairs
    else:
        pairs = PairList(pairs)

    if group:
        _tags = pairs.tags[:, 0] + "-->" + pairs.tags[:, 1]
        _tags, mask = np.unique(_tags, return_inverse=True)
        if tags is None:
            tags = _tags

        values = np.linalg.eigvalsh(pairs.J_S_meV)
        dists = pairs.distance
        if colors is None:
            colors = px.colors.qualitative.D3
            colors = colors * (len(tags) // len(colors) + 1)

        # Create figure
        fig = go.Figure()
        for i in range(len(tags)):
            fig.add_trace(
                go.Scatter(
                    name="Eigenvalues 1: " + tags[i],
                    x=dists[mask == i],
                    y=values[mask == i, 0],
                    mode="markers",
                    marker=dict(
                        size=marker_size,
                        opacity=marker_opacity,
                        color=colors[i],
                        symbol="circle-open",
                    ),
                )
            )
            fig.add_trace(
                go.Scatter(
                    name="Eigenvalues 2: " + tags[i],
                    x=dists[mask == i],
                    y=values[mask == i, 1],
                    mode="markers",
                    marker=dict(
                        size=marker_size,
                        opacity=marker_opacity,
                        color=colors[i],
                        symbol="cross",
                    ),
                )
            )
            fig.add_trace(
                go.Scatter(
                    name="Eigenvalues 3: " + tags[i],
                    x=dists[mask == i],
                    y=values[mask == i, 2],
                    mode="markers",
                    marker=dict(
                        size=marker_size,
                        opacity=marker_opacity,
                        color=colors[i],
                        symbol="x",
                    ),
                )
            )

    else:
        if colors is None:
            colors = px.colors.qualitative.D3
        # Create figure
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                name="Eigenvalues 1",
                x=pairs.distance,
                y=np.linalg.eigvalsh(pairs.J_S_meV)[:, 0],
                mode="markers",
                marker=dict(size=marker_size, opacity=marker_opacity, color=colors[0]),
            )
        )
        fig.add_trace(
            go.Scatter(
                name="Eigenvalues 2",
                x=pairs.distance,
                y=np.linalg.eigvalsh(pairs.J_S_meV)[:, 1],
                mode="markers",
                marker=dict(size=marker_size, opacity=marker_opacity, color=colors[1]),
            )
        )
        fig.add_trace(
            go.Scatter(
                name="Eigenvalues 3",
                x=pairs.distance,
                y=np.linalg.eigvalsh(pairs.J_S_meV)[:, 2],
                mode="markers",
                marker=dict(size=marker_size, opacity=marker_opacity, color=colors[2]),
            )
        )

    # Create layout
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        title=title,
        xaxis_title="Pair distance [Ang]",
        yaxis_title="Eigenvalues of symmetric exchange [meV]",
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
        ),
        showlegend=legend,
    )

    return fig


def plot_1D_convergence(
    files: list[str],
    atol: float = 1e-4,
    rtol: float = 1e-4,
    marker_size: float = 10,
    marker_opacity: float = 1,
    width: int = 800,
    height: int = 500,
    title: Union[None, str] = None,
) -> go.Figure:
    """Reads output files and create a plot for the convergence test.

    Parameters
    ----------
    files : list[str]
        The path to the output files .pkl
    atol : float, optional
        Absolute tolerance to convergence, by default 1e-4
    rtol : float, optional
        Relative tolerance to convergence, by default 1e-4
    marker_size : float, optional
        Size of the markers, by default 10
    marker_opacity : float, optional
        Opacity of the markers, by default 1
    width : int, optional
        Width of the figure, by default 800
    height : int, optional
        Height of the figure, by default 500
    title : Union[None, str], optional
        Title of the figure, if set to None, then title is not
        generated, by default None

    Returns
    -------
    go.Figure
        Plotly figure

    Raises
    ------
    Exception
        Not enough paths to compare!
    Exception
        Multiple spin models in files!
    Exception
        Convergence parameter not found!
    """

    # check number of files
    if len(files) < 2:
        raise Exception("Not enough paths to compare!")

    # load data
    builders = []
    spin_models = []
    ksets = []
    esets = []
    esetps = []
    for f in files:
        builders.append(load_Builder(f))
        spin_models.append(builders[-1].spin_model)
        ksets.append(builders[-1].kspace.NK)
        esets.append(builders[-1].contour.eset)
        esetps.append(builders[-1].contour.esetp)
    builders = np.array(builders, dtype=object)

    # check spin models
    spin_models = np.unique(np.array(spin_models))
    if len(spin_models) != 1:
        raise Exception(f"Multiple spin models in files: {spin_models}!")

    # check other parameters
    # number of parameters in files
    ksets = np.unique(np.array(ksets))
    esets = np.unique(np.array(esets))
    esetps = np.unique(np.array(esetps))
    # check convergence type
    mode = None
    conv_params = None
    if len(ksets) == 1 and len(esets) == 1 and len(esetps) != 1:
        mode = "Esetp"
        conv_params = [b.contour.esetp for b in builders]
    if len(ksets) == 1 and len(esets) != 1 and len(esetps) == 1:
        mode = "Eset"
        conv_params = [b.contour.eset for b in builders]
    if len(ksets) != 1 and len(esets) == 1 and len(esetps) == 1:
        mode = "Total number of K points"
        conv_params = [b.kspace.NK for b in builders]
    if mode is None:
        raise Exception("Convergence parameter not found!")

    # sort
    conv_params = np.array(conv_params)
    idx = np.argsort(conv_params)
    conv_params = conv_params[idx]
    builders = builders[idx]

    # get all data
    compare = []
    for b in builders:
        dat = np.hstack([b.magnetic_entities.K_meV.flatten(), b.pairs.J_meV.flatten()])
        compare.append(dat[dat != None].astype(float))
    try:
        compare = np.array(compare).T
    except:
        raise Exception("Number of pairs or magnetic entites changed between Builders!")

    # add lines
    fig = go.Figure()
    for i in range(len(compare)):
        fig.add_trace(
            go.Scatter(
                x=conv_params,
                y=compare[i],
                mode="markers+lines",
                marker=dict(
                    size=marker_size, opacity=marker_opacity, symbol="circle-open"
                ),
            )
        )

    # turn back
    compare = compare.T

    # check for convergence
    converged = False
    for i in range(int(len(compare) - 1)):
        if np.allclose(compare[i], compare[-1], rtol=rtol, atol=atol):
            fig.add_vline(
                x=(conv_params[i] + conv_params[i + 1]) / 2,
                line_width=3,
                line_color="red",
            )
            converged = True
            break

    # if not converged
    if converged:
        fig.add_annotation(
            x=0.99,
            y=0.99,
            showarrow=False,
            text=f"Convergence reached compared to highest parameter (atol={atol:.2e}, rtol={rtol:.2e})",
            textangle=0,
            xanchor="right",
            xref="paper",
            yref="paper",
        )

    else:
        fig.add_annotation(
            x=0.99,
            y=0.99,
            showarrow=False,
            text=f"Convergence not reached (atol={atol:.2e}, rtol={rtol:.2e})",
            textangle=0,
            xanchor="right",
            xref="paper",
            yref="paper",
        )

    # Create layout
    fig.update_layout(
        autosize=False,
        width=width,
        height=height,
        title=title,
        xaxis_title=f"{mode} [ ]",
        yaxis_title="System vector [meV]",
        xaxis=dict(
            tickmode="array",
            tickvals=conv_params,
            ticktext=[str(i) for i in conv_params],
            showgrid=True,
            gridwidth=1,
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
        ),
        showlegend=False,
    )
    return fig


if __name__ == "__main__":
    pass
