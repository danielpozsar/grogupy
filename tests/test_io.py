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
import pytest
import sisl

from grogupy.io.io import read_magnopy
from grogupy.io.utilities import decipher, decipher_all_by_pos, decipher_all_by_tag


def test_parse_magnopy():
    out = read_magnopy(
        "/Users/danielpozsar/Documents/oktatás/elte/phd/grogu_project/tests/io_matlab_result.magnopy.txt"
    )
    assert out["cell"]["unit"] == "a"
    assert out["atoms"]["unit"] == "a"
    atoms = [
        dict(tag="Te1", xyz=np.array([1.8955, 1.0943, 13.1698])),
        dict(tag="Te2", xyz=np.array([1.8955, 1.0943, 7.4002])),
        dict(tag="Ge3", xyz=np.array([-0.0000, 2.1887, 10.2850])),
        dict(tag="Fe4", xyz=np.array([-0.0000, 0.0000, 11.6576])),
        dict(tag="Fe5", xyz=np.array([-0.0000, 0.0000, 8.9124])),
        dict(tag="Fe6", xyz=np.array([1.8955, 1.0944, 10.2850])),
    ]
    assert len(out["atoms"]["magnetic_entities"]) == len(atoms)
    for at1, at2 in zip(out["atoms"]["magnetic_entities"], atoms):
        assert at1["tag"] == at2["tag"]
        assert (at1["xyz"] == at2["xyz"]).all()
    assert out["exchange"]["unit"] == "m"
    pairs = [
        {
            "tag1": "Fe4",
            "tag2": "Fe5",
            "Ruc": np.array([0, 0, 0]),
            "iso": -82.0854,
            "DM": np.array([1.2557e-01, -8.2199e-04, 6.9668e-08]),
            "S": np.array(
                [-6.0237e-01, -8.3842e-01, -3.2278e-04, -1.2166e-05, -3.3923e-05]
            ),
            "xyz1": np.array([-0.0, 0.0, 11.6576]),
            "xyz2": np.array([-0.0, 0.0, 8.9124]),
        },
        {
            "tag1": "Fe4",
            "tag2": "Fe6",
            "Ruc": np.array([0, 0, 0]),
            "iso": -41.9627,
            "DM": np.array([1.1205e00, -1.9532e00, 1.8386e-03]),
            "S": np.array(
                [2.6007e-01, -1.3243e-04, 1.2977e-01, -6.9979e-02, -4.2066e-02]
            ),
            "xyz1": np.array([-0.0, 0.0, 11.6576]),
            "xyz2": np.array([1.8955, 1.0944, 10.285]),
        },
        {
            "tag1": "Fe4",
            "tag2": "Fe4",
            "Ruc": np.array([1, 0, 0]),
            "iso": 11.3817,
            "DM": np.array([-0.027065, 5.0079, 1.2495]),
            "S": np.array(
                [2.5899e-01, 6.1356e-01, 1.8352e-04, -8.2489e-06, -5.9116e-02]
            ),
            "xyz1": np.array([-0.0, 0.0, 11.6576]),
            "xyz2": np.array([-0.0, 0.0, 11.6576]),
        },
        {
            "tag1": "Fe4",
            "tag2": "Fe5",
            "Ruc": np.array([1, 0, 0]),
            "iso": -2.9464,
            "DM": np.array([1.7, 0.0069825, 6.4657]),
            "S": np.array([4.4323e-01, 5.6997e-02, 1.7739e-05, 1.4942e-01, 1.0770e-05]),
            "xyz1": np.array([-0.0, 0.0, 11.6576]),
            "xyz2": np.array([-0.0, 0.0, 8.9124]),
        },
        {
            "tag1": "Fe4",
            "tag2": "Fe6",
            "Ruc": np.array([1, 0, 0]),
            "iso": -1.9722,
            "DM": np.array([-0.044414, 0.34777, 0.55124]),
            "S": np.array([0.19364, -0.10179, -0.057654, 0.023297, 0.033722]),
            "xyz1": np.array([-0.0, 0.0, 11.6576]),
            "xyz2": np.array([1.8955, 1.0944, 10.285]),
        },
        {
            "tag1": "Fe4",
            "tag2": "Fe4",
            "Ruc": np.array([2, 0, 0]),
            "iso": -2.5085,
            "DM": np.array([0.015126, 0.020638, -0.26104]),
            "S": np.array([-0.145, -0.021424, 6.948e-05, 3.0356e-05, -0.18409]),
            "xyz1": np.array([-0.0, 0.0, 11.6576]),
            "xyz2": np.array([-0.0, 0.0, 11.6576]),
        },
    ]
    assert len(out["exchange"]["pairs"]) == len(pairs)
    for p1, p2 in zip(out["exchange"]["pairs"], pairs):
        assert p1["tag1"] == p2["tag1"]
        assert p1["tag2"] == p2["tag2"]
        assert (p1["Ruc"] == p2["Ruc"]).all()
        assert p1["iso"] == p2["iso"]
        assert (p1["DM"] == p2["DM"]).all()
        assert (p1["S"] == p2["S"]).all()
        assert (p1["xyz1"] == p2["xyz1"]).all()
        assert (p1["xyz2"] == p2["xyz2"]).all()
    assert out["on-site"]["unit"] == "m"
    atoms = [{"tag": "Fe4", "K": np.array([0.16339, 0.16068, 0.0, 0.0, 0.0, 0.0])}]
    assert len(out["on-site"]["magnetic_entities"]) == len(atoms)
    for at1, at2 in zip(out["on-site"]["magnetic_entities"], atoms):
        assert at1["tag"] == at2["tag"]
        assert (at1["K"] == at2["K"]).all()


def test_decipher_all_by_pos():
    dh = sisl.get_sile(
        "/Users/danielpozsar/Downloads/nojij/Fe3GeTe2/monolayer/soc/lat3_791/Fe3GeTe2.fdf"
    ).read_hamiltonian()
    out = read_magnopy(
        "/Users/danielpozsar/Documents/oktatás/elte/phd/grogu_project/tests/io_matlab_result.magnopy.txt"
    )
    magnetic_entities = out["atoms"]["magnetic_entities"]
    pairs = out["exchange"]["pairs"]
    cmagnetic_entities, cpairs = decipher_all_by_pos(dh, magnetic_entities, pairs)
    magnetic_entities = [
        {"atom": 0},
        {"atom": 1},
        {"atom": 2},
        {"atom": 3},
        {"atom": 4},
        {"atom": 5},
    ]
    pairs = [
        {"ai": 3, "aj": 4, "Ruc": np.array([0, 0, 0])},
        {"ai": 3, "aj": 5, "Ruc": np.array([0, 0, 0])},
        {"ai": 3, "aj": 3, "Ruc": np.array([1, 0, 0])},
        {"ai": 3, "aj": 4, "Ruc": np.array([1, 0, 0])},
        {"ai": 3, "aj": 5, "Ruc": np.array([1, 0, 0])},
        {"ai": 3, "aj": 3, "Ruc": np.array([2, 0, 0])},
    ]

    assert len(magnetic_entities) == len(cmagnetic_entities)
    for m1, m2 in zip(magnetic_entities, cmagnetic_entities):
        assert m1["atom"] == m2["atom"]
    assert len(pairs) == len(cpairs)
    for p1, p2 in zip(pairs, cpairs):
        assert p1["ai"] == p2["ai"]
        assert p1["aj"] == p2["aj"]
        assert (p1["Ruc"] == p2["Ruc"]).all()


def test_decipher_all_by_tag():
    out = read_magnopy(
        "/Users/danielpozsar/Documents/oktatás/elte/phd/grogu_project/tests/io_test_matlab.magnopy.txt"
    )
    magnetic_entities = out["atoms"]["magnetic_entities"]
    pairs = out["exchange"]["pairs"]
    cmagnetic_entities, cpairs = decipher_all_by_tag(magnetic_entities, pairs)
    magnetic_entities = [{"atom": [3]}, {"atom": [4]}, {"atom": [5]}]
    pairs = [
        {"ai": 0, "aj": 1, "Ruc": np.array([0, 0, 0])},
        {"ai": 0, "aj": 2, "Ruc": np.array([0, 0, 0])},
        {"ai": 0, "aj": 0, "Ruc": np.array([1, 0, 0])},
        {"ai": 0, "aj": 1, "Ruc": np.array([1, 0, 0])},
        {"ai": 0, "aj": 2, "Ruc": np.array([1, 0, 0])},
        {"ai": 0, "aj": 0, "Ruc": np.array([2, 0, 0])},
    ]
    print(cpairs)
    assert len(magnetic_entities) == len(cmagnetic_entities)
    for m1, m2 in zip(magnetic_entities, cmagnetic_entities):
        assert m1["atom"] == m2["atom"]
    assert len(pairs) == len(cpairs)
    for p1, p2 in zip(pairs, cpairs):
        assert p1["ai"] == p2["ai"]
        assert p1["aj"] == p2["aj"]
        assert (p1["Ruc"] == p2["Ruc"]).all()


@pytest.mark.parametrize(
    "tag, atom, l, orb",
    [
        ("0Te(o:1)", [0], None, [[1]]),
        ("0Te(o:1-2)", [0], None, [[1, 2]]),
        ("0Te(l:1)", [0], [[1]], None),
        ("0Te(l:1-2)", [0], [[1, 2]], None),
        ("0Te(l:All)", [0], [[None]], None),
        ("1Te(o:1)", [1], None, [[1]]),
        ("1Te(o:1-2)", [1], None, [[1, 2]]),
        ("1Te(l:1)", [1], [[1]], None),
        ("1Te(l:1-2)", [1], [[1, 2]], None),
        ("1Te(l:All)", [1], [[None]], None),
        ("0Te(o:1)--0Te(o:1)", [0, 0], None, [[1], [1]]),
        ("0Te(o:1)--0Te(o:1-2)", [0, 0], None, [[1], [1, 2]]),
        ("0Te(o:1)--1Te(o:1)", [0, 1], None, [[1], [1]]),
        ("0Te(o:1)--1Te(o:1-2)", [0, 1], None, [[1], [1, 2]]),
    ],
)
def test_decipher(tag, atom, l, orb):
    catom, cl, corb = decipher(tag)

    print(catom, atom)
    print(cl, l)
    print(corb, orb)

    assert catom == atom
    assert cl == l
    assert corb == orb


@pytest.mark.parametrize(
    "tag",
    [
        ("0Te(a:1)"),
        ("Te(o:1)"),
        ("0Te(o:all)"),
        ("0Te(l:allee)"),
        ("0Te(l:allee-allee)"),
        ("0Te(l:allee--allee)"),
        ("0Te(o:1)--0Te(l:1)"),
        ("0Te(o:1)--0Te(l:1-2)"),
        ("0Te(o:1)--0Te(l:All)"),
        ("0Te(o:1)--1Te(l:1)"),
        ("0Te(o:1)--1Te(l:1-2)"),
        ("0Te(o:1)--1Te(l:All)"),
    ],
)
def test_raise_decipher(tag):
    with pytest.raises(Exception):
        atom, l, orb = decipher(tag)
        print(atom, l, orb)
