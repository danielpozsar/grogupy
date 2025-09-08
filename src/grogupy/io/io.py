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

import importlib.util
import pickle
import warnings
from os.path import join
from typing import Union

import h5py
import numpy as np

from grogupy import CONFIG, __version__
from grogupy._core.utilities import arrays_lists_equal, make_contour, make_kset
from grogupy.batch.timing import DefaultTimer
from grogupy.physics import Builder, Contour, Hamiltonian, Kspace, MagneticEntity, Pair

from .._core.io_utilities import strip_dict_structure

# Only print on MPI root node
PRINTING = True
if CONFIG.is_CPU:
    if CONFIG.MPI_loaded:
        from mpi4py import MPI

        rank = MPI.COMM_WORLD.rank
        if rank != 0:
            PRINTING = False


def load_DefaultTimer(infile: Union[str, dict]) -> DefaultTimer:
    """Recreates the instance from a pickled state.

    Parameters
    ----------
    infile : Union[str, dict]
        Either the path to the file or the appropriate
        dictionary for the setup

    Returns
    -------
    DefaultTimer
        The DefaultTimer instance that was loaded
    """

    # load pickled file
    if isinstance(infile, str):
        if not infile.endswith(".pkl"):
            infile += ".pkl"
        with open(infile, "rb") as file:
            infile = pickle.load(file)

    # build instance
    out = object.__new__(DefaultTimer)
    out.__setstate__(infile)

    return out


def load_Contour(infile: Union[str, dict]) -> Contour:
    """Recreates the instance from a pickled state.

    Parameters
    ----------
    infile : Union[str, dict]
        Either the path to the file or the appropriate
        dictionary for the setup

    Returns
    -------
    Contour
        The Contour instance that was loaded
    """

    # load pickled file
    if isinstance(infile, str):
        if not infile.endswith(".pkl"):
            infile += ".pkl"
        with open(infile, "rb") as file:
            infile = pickle.load(file)

    # build instance
    out = object.__new__(Contour)
    out.__setstate__(infile)

    if len(out.samples) == 0:
        try:
            out.samples, out.weights = make_contour(
                out.emin, out.emax, out.eset, out.esetp
            )
        except:
            print("Failed to recreate contour!")

    return out


def load_Kspace(infile: Union[str, dict]) -> Kspace:
    """Recreates the instance from a pickled state.

    Parameters
    ----------
    infile : Union[str, dict]
        Either the path to the file or the appropriate
        dictionary for the setup

    Returns
    -------
    Kspace
        The Kspace instance that was loaded
    """

    # load pickled file
    if isinstance(infile, str):
        if not infile.endswith(".pkl"):
            infile += ".pkl"
        with open(infile, "rb") as file:
            infile = pickle.load(file)

    # build instance
    out = object.__new__(Kspace)
    out.__setstate__(infile)

    if len(out.kpoints) == 0:
        try:
            out.kpoints = make_kset(out.kset)
            out.weights = np.ones(len(out.kpoints)) / len(out.kpoints)
        except:
            print("Failed to recreate kspace!")

    return out


def load_MagneticEntity(infile: Union[str, dict]) -> MagneticEntity:
    """Recreates the instance from a pickled state.

    Parameters
    ----------
    infile : Union[str, dict]
        Either the path to the file or the appropriate
        dictionary for the setup

    Returns
    -------
    MagneticEntity
        The MagneticEntity instance that was loaded
    """

    # load pickled file
    if isinstance(infile, str):
        if not infile.endswith(".pkl"):
            infile += ".pkl"
        with open(infile, "rb") as file:
            infile = pickle.load(file)

    # build instance
    out = object.__new__(MagneticEntity)
    out.__setstate__(infile)

    return out


def load_Pair(infile: Union[str, dict]) -> Pair:
    """Recreates the instance from a pickled state.

    Parameters
    ----------
    infile : Union[str, dict]
        Either the path to the file or the appropriate
        dictionary for the setup

    Returns
    -------
    Pair
        The Pair instance that was loaded
    """

    # load pickled file
    if isinstance(infile, str):
        if not infile.endswith(".pkl"):
            infile += ".pkl"
        with open(infile, "rb") as file:
            infile = pickle.load(file)

    # build instance
    out = object.__new__(Pair)
    out.__setstate__(infile)

    return out


def load_Hamiltonian(infile: Union[str, dict]) -> Hamiltonian:
    """Recreates the instance from a pickled state.

    Parameters
    ----------
    infile : Union[str, dict]
        Either the path to the file or the appropriate
        dictionary for the setup

    Returns
    -------
    Hamiltonian
        The Hamiltonian instance that was loaded
    """

    # load pickled file
    if isinstance(infile, str):
        if not infile.endswith(".pkl"):
            infile += ".pkl"
        with open(infile, "rb") as file:
            infile = pickle.load(file)

    # build instance
    out = object.__new__(Hamiltonian)
    out.__setstate__(infile)

    return out


def load_Builder(infile: Union[str, dict]) -> Builder:
    """Recreates the instance from a pickled state.

    Parameters
    ----------
    infile : Union[str, dict]
        Either the path to the file or the appropriate
        dictionary for the setup

    Returns
    -------
    Builder
        The Builder instance that was loaded
    """

    # load pickled file
    if isinstance(infile, str):
        if not infile.endswith(".pkl"):
            infile += ".pkl"
        with open(infile, "rb") as file:
            infile = pickle.load(file)

    # build instance
    out = object.__new__(Builder)
    out.__setstate__(infile)

    if len(out.contour.samples) == 0:
        try:
            out.contour.samples, out.contour.weights = make_contour(
                out.contour.emin, out.contour.emax, out.contour.eset, out.contour.esetp
            )
        except:
            print("Failed to recreate contour!")
    if len(out.kspace.kpoints) == 0:
        try:
            out.kspace.kpoints = make_kset(out.kspace.kset)
            out.kspace.weights = np.ones(len(out.kspace.kpoints)) / len(
                out.kspace.kpoints
            )
        except:
            print("Failed to recreate kspace!")

    return out


def load(
    infile: Union[str, dict]
) -> Union[DefaultTimer, Contour, Kspace, MagneticEntity, Pair, Hamiltonian, Builder]:
    """Recreates the instance from a pickled state.

    Parameters
    ----------
    infile : Union[str, dict]
        Either the path to the file or the appropriate
        dictionary for the setup

    Returns
    -------
    Union[DefaultTimer, Contour, Kspace, MagneticEntity, Pair, Hamiltonian, Builder]
        The instance that was loaded
    """
    # load pickled file
    if isinstance(infile, str):
        if not infile.endswith(".pkl"):
            infile += ".pkl"
        with open(infile, "rb") as file:
            dat = pickle.load(file)
    else:
        dat = infile

    if list(dat.keys()) == [
        "times",
        "kspace",
        "contour",
        "hamiltonian",
        "magnetic_entities",
        "pairs",
        "_Builder__low_memory_mode",
        "_Builder__greens_function_solver",
        "_Builder__max_g_per_loop",
        "_Builder__parallel_mode",
        "_Builder__architecture",
        "_Builder__apply_spin_model",
        "_Builder__spin_model",
        "_Builder__ref_xcf_orientations",
        "_rotated_hamiltonians",
        "SLURM_ID",
        "_Builder__version",
    ]:
        return load_Builder(infile)

    elif list(dat.keys()) == [
        "times",
        "kspace",
        "contour",
        "hamiltonian",
        "magnetic_entities",
        "pairs",
        "ref_xcf_orientations",
        "_rotated_hamiltonians",
        "SLURM_ID",
        "_Builder__version",
    ]:
        b = load_Builder(infile)
        if PRINTING:
            warnings.warn(
                f"There is a mismatch between Builder ({b.version}) and current ({__version__}) version!"
            )
        return b

    elif list(dat.keys()) == [
        "times",
        "_dh",
        "_ds",
        "infile",
        "_spin_state",
        "_Hamiltonian__dh_ds_id",
        "H",
        "S",
        "scf_xcf_orientation",
        "orientation",
        "_Hamiltonian__no",
        "_Hamiltonian__cell",
        "_Hamiltonian__sc_off",
        "_Hamiltonian__uc_in_sc_index",
    ]:
        return load_Hamiltonian(infile)
    elif list(dat.keys()) == [
        "_Pair__dh_ds_id",
        "cell",
        "M1",
        "M2",
        "supercell_shift",
        "_Gij",
        "_Gji",
        "energies",
        "_J",
    ]:
        return load_Pair(infile)
    elif list(dat.keys()) == [
        "infile",
        "_MagneticEntity__dh_ds_id",
        "_MagneticEntity__cell",
        "_atom",
        "_l",
        "_orbital_box_indices",
        "_total_orbital_box_indices",
        "_tags",
        "_mulliken",
        "_xyz",
        "_Vu1",
        "_Vu2",
        "_Gii",
        "energies",
        "_K",
        "_K_consistency",
    ]:
        return load_MagneticEntity(infile)
    elif list(dat.keys()) == ["times", "_Kspace__kset", "kpoints", "weights"]:
        return load_Kspace(infile)
    elif list(dat.keys()) == [
        "times",
        "_Contour__automatic_emin",
        "_eigfile",
        "_emin",
        "_emax",
        "_eset",
        "_esetp",
        "samples",
        "weights",
    ]:
        return load_Contour(infile)
    elif list(dat.keys()) == ["_DefaultTimer__start_measure", "_times"]:
        return load_DefaultTimer(infile)
    else:
        raise Exception("Unknown pickle format!")


def save(
    object: Union[
        DefaultTimer, Contour, Kspace, MagneticEntity, Pair, Hamiltonian, Builder
    ],
    path: str,
    compress: int = 2,
) -> None:
    """Saves the instance from a pickled state.

    The compression level can be set to 0,1,2,3,4. Every other value defaults to 2.

    0. This means that there is no compression at all.

    1. This means, that the keys "_dh" and "_ds" are set
       to None, because othervise the loading would be dependent
       on the sisl version

    2. This contains compression 1, but sets the keys "Gii", "Gij",
       "Gji", "Vu1" and "Vu2" to [], to save space

    3. This contains compression 1 and 2, but sets the keys "S", "H",
       to [], to save space

    4. This contains compression 1, 2 and 3, but sets the keys "kpoints",
       "samples", "weights" (for kpoints and energy points) to [], to
       save space

    Parameters
    ----------
    object : Union[DefaultTimer, Contour, Kspace, MagneticEntity, Pair, Hamiltonian, Builder]
        Object from the grogupy library
    path: str
        The path to the output file
    compress: int, optional
        The level of lossy compression of the output pickle, by default 2
    """

    # check if the object is ours
    if object.__module__.split(".")[0] == "grogupy":
        # add pkl so we know it is pickled
        if not path.endswith(".pkl"):
            path += ".pkl"

        # the dictionary to be saved
        out_dict = object.__getstate__()

        # remove large objects to save memory or to avoid sisl loading errors
        if compress == 0:
            pass
        elif compress == 1:
            out_dict = strip_dict_structure(out_dict, pops=["_dh", "_ds"], setto=None)
        elif compress == 3:
            out_dict = strip_dict_structure(out_dict, pops=["_dh", "_ds"], setto=None)
            out_dict = strip_dict_structure(
                out_dict,
                pops=[
                    "S",
                    "H",
                    "_Gii",
                    "_Gij",
                    "_Gji",
                    "_Vu1",
                    "_Vu2",
                ],
                setto=[],
            )
        elif compress == 4:
            out_dict = strip_dict_structure(out_dict, pops=["_dh", "_ds"], setto=None)
            out_dict = strip_dict_structure(
                out_dict,
                pops=[
                    "S",
                    "H",
                    "kpoints",
                    "samples",
                    "weights",
                    "_Gii",
                    "_Gij",
                    "_Gji",
                    "_Vu1",
                    "_Vu2",
                ],
                setto=[],
            )
        # compress 2 is the default
        else:
            out_dict = strip_dict_structure(out_dict, pops=["_dh", "_ds"], setto=None)
            out_dict = strip_dict_structure(
                out_dict,
                pops=[
                    "_Gii",
                    "_Gij",
                    "_Gji",
                    "_Vu1",
                    "_Vu2",
                ],
                setto=[],
            )
        # write to file
        with open(path, "wb") as f:
            pickle.dump(out_dict, f)

    else:
        raise Exception(
            f"The object is from package {object.__module__.split('.')[0]} instead of grogupy!"
        )


def save_grogupy(
    builder: Builder,
    path: Union[None, str] = None,
) -> Union[None, str]:
    """Creates a grogupy output file.

    Parameters
    ----------
    builder: Builder
        The system that we want to save
    path: Union[None, str], optional
        Output path or if None it returns a string, by default None

    Returns
    -------
    out: Union[None, str]
        A string of the output file or None, in which case it is written
        to the path
    """

    if path is not None:
        if not path.endswith(".grogupy.txt"):
            path += ".grogupy.txt"

    section = "--------------------------------------------------------------------------------"
    subsection = "----------------------------------------"
    newline = "\n"

    out = ""
    out += builder.__str__()[:-1]
    out += newline

    out += "Magnetic entities" + newline
    out += f"Number of magnetic entities {len(builder.magnetic_entities)}" + newline

    for mag_ent in builder.magnetic_entities:
        out += subsection + newline
        out += "Tag\t\t\t" + mag_ent.tag + newline
        out += (
            "Unique ID:\t"
            + "\t".join(map(lambda s: f"{s:d}", mag_ent.dh_ds_id))
            + newline
        )
        out += "Atom\t\t" + " ".join(map(lambda s: f"{s:d}", mag_ent._atom))
        out += newline
        out += "Shell"
        for shell in mag_ent._l:
            out += "\t\t" + " ".join(
                map(lambda s: "None" if s is None else f"{s:d}", shell)
            )
            out += newline
        out += "Orbital box\t" + " ".join(
            map(lambda s: f"{s:d}", mag_ent._orbital_box_indices)
        )
        out += newline
        out += "Total orbital box\t" + " ".join(
            map(lambda s: f"{s:d}", mag_ent._total_orbital_box_indices)
        )
        out += newline
        out += "Position\tx [Ang]\t\ty [Ang]\t\tz [Ang]" + newline
        for xyz in mag_ent._xyz:
            out += "\t\t" + "\t".join(map(lambda s: f"{s:.8f}", xyz))
            out += newline
        out += "Energies [eV]" + newline
        for e in mag_ent.energies:
            out += "\t\t" + "\t".join(map(lambda s: f"{s:.8e}", e))
            out += newline
    out += subsection + newline
    out += section + newline

    out += "Pairs" + newline
    out += f"Number of pairs {len(builder.pairs)}" + newline
    for pair in builder.pairs:
        out += subsection + newline
        out += "Tags\t\t" + pair.tags[0] + "\t" + pair.tags[1] + newline
        out += (
            "Unique ID:\t" + "\t".join(map(lambda s: f"{s:d}", pair.dh_ds_id)) + newline
        )
        out += "Cell shift\t" + "\t".join(map(str, pair.supercell_shift))
        out += f"\t# Distance: {pair.distance} Ang" + newline
        out += "Energies [eV]" + newline
        for e in pair.energies:
            out += "\t\t" + "\t".join(map(lambda s: f"{s:.8e}", e))
            out += newline
    out += subsection + newline
    out += section + newline
    # save times
    out += f"Times\n"
    out += f"Builder\n"
    times = builder.times.times
    for k, v in times.items():
        out += f"\t\t{k}\t\t{v}"
        out += newline
    out += f"Hamiltonian\n"
    times = builder.hamiltonian.times.times
    for k, v in times.items():
        out += f"\t\t{k}\t\t{v}"
        out += newline
    out += f"Kspace\n"
    times = builder.kspace.times.times
    for k, v in times.items():
        out += f"\t\t{k}\t\t{v}"
        out += newline
    out += f"Contour\n"
    times = builder.contour.times.times
    for k, v in times.items():
        out += f"\t\t{k}\t\t{v}"
        out += newline
    out += section + newline
    # compare Mullikens
    mismatch = False
    base = builder.magnetic_entities[0]
    for m in builder.magnetic_entities:
        if m._mulliken is None and base._mulliken is None:
            pass
        else:
            if not arrays_lists_equal(m._mulliken, base._mulliken):
                mismatch = True
                break
    if not mismatch and base._mulliken is not None:
        out += "Mulliken" + newline
        for m in builder.magnetic_entities[0]._mulliken.T:
            out += "\t".join(map(lambda s: f"{s:.8e}", m))
            out += newline
        out += section + newline

    if path is None:
        return out

    with open(path, "w") as file:
        file.write(out)


def read_grogupy(file: str):
    """This function reads the grogupy input file and returns a Builder object

    Parambeters
    ----------
    file: str
        Path to the ``grogupy`` input file

    Returns
    -------
    Builder
        The Builder object

    Exception
    ---------
        If there is an unrecognised section
    """

    # read file
    with open(file, "r") as f:
        lines = f.readlines()

    for i, l in enumerate(lines):
        if l.find("#") != -1:
            lines[i] = l[: l.find("#")] + "\n"

    # this is a dense line that splits the magnopy file to sections,
    # then splits the sections by lines
    # this creates a list if lists of strings
    sections = [
        sec.split("\n")
        for sec in "".join(lines).split(
            "--------------------------------------------------------------------------------\n"
        )[1:-1]
    ]

    out = dict()
    out["_Builder__apply_spin_model"] = True
    # iterate over sections
    for section in sections:
        # metadata section
        if section[0] == "Metadata":
            out["hamiltonian"] = dict()
            for line in section:
                line = line.replace("\t", "").split(":")
                if line[0] == "grogupy version":
                    out["_Builder__version"] = line[1]
                elif line[0] == "Architecture":
                    out["_Builder__architecture"] = line[1]
                elif line[0] == "SLURM job ID":
                    out["SLURM_ID"] = line[1]
                elif line[0] == "Input file":
                    out["hamiltonian"]["infile"] = line[1]
        # solver section
        elif section[0] == "Solver":
            for line in section:
                line = line.replace("\t", "").split(":")
                if line[0] == "Parallelization is over":
                    out["_Builder__parallel_mode"] = line[1]
                elif line[0] == "Solver used for Greens function calculation":
                    out["_Builder__greens_function_solver"] = line[1]
                elif line[0] == "Maximum number of Greens function samples per batch":
                    out["_Builder__max_g_per_loop"] = line[1]
        # hamiltonian section
        elif section[0] == "Hamiltonian":
            for line in section:
                line = line.split(":")
                if line[0] == "Spin model":
                    out["_Builder__spin_model"] = line[1].replace("\t", "")
                elif line[0] == "Spin mode":
                    out["hamiltonian"]["_spin_state"] = line[1].replace("\t", "")
                elif line[0] == "Number of orbitals":
                    out["hamiltonian"]["_Hamiltonian__no"] = int(line[1])
                elif line[0] == "Unique ID":
                    out["hamiltonian"]["_Hamiltonian__dh_ds_id"] = np.array(
                        line[1].split(), dtype=int
                    )
        # cell section
        elif section[0] == "Cell [Ang]":
            cell = []
            for line in section[1:-1]:
                cell.append(line.split())
            cell = np.array(cell, dtype=float)
            out["hamiltonian"]["_Hamiltonian__cell"] = cell
        # exchange field section
        elif section[0] == "Exchange field rotations":
            line = section[1]
            line = line.replace("\t", "").split(":")
            if line[0] == "DFT axis":
                out["hamiltonian"]["scf_xcf_orientation"] = np.array(
                    line[1][1:-1].split(), dtype=float
                )
                out["hamiltonian"]["orientation"] = np.array(
                    line[1][1:-1].split(), dtype=float
                )
            ref_scf_orientation = []
            for line in section[3:-1]:
                line = line.split()
                if line[-1] == "-->":
                    if len(ref_scf_orientation) != 0:
                        ref_scf_orientation[-1]["vw"] = np.array(vw, dtype=float)
                    ref_scf_orientation.append({"o": np.array(line[:-1], dtype=float)})
                    vw = []
                else:
                    vw.append(np.array(line, dtype=float))
            if len(ref_scf_orientation) != 0:
                ref_scf_orientation[-1]["vw"] = np.array(vw, dtype=float)
            vw = []
            out["_Builder__ref_xcf_orientations"] = ref_scf_orientation
        # kspace section
        elif section[0] == "Kspace":
            out["kspace"] = dict()
            line = section[2]
            line = line.replace("\t", "").split(":")
            out["kspace"]["_Kspace__kset"] = np.array(line[1][1:-1].split(), dtype=int)
            out["kspace"]["kpoints"] = []
        # coontour section
        elif section[0] == "Contour":
            out["contour"] = dict()
            for line in section[1:-1]:
                line = line.replace("\t", "").split(":")
                if line[0] == "Eset":
                    out["contour"]["_eset"] = int(line[1])
                if line[0] == "Esetp":
                    out["contour"]["_esetp"] = int(line[1])
                if line[0] == "Ebot":
                    out["contour"]["_emin"] = float(line[1])
                if line[0] == "Etop":
                    out["contour"]["_emax"] = float(line[1])
        # magnetic entities section
        elif section[0] == "Magnetic entities":
            NM = 0
            if " ".join(section[1].split()[:4]) == "Number of magnetic entities":
                NM = int(section[1].split()[-1])
            mag_ent_list = []
            mag_ent = dict()
            mag_ent["_l"] = []
            mag_ent["_xyz"] = []
            mag_ent["energies"] = []
            continue_writing = None
            for line in section[3:-1]:
                if line.startswith("----------"):
                    mag_ent["infile"] = out["hamiltonian"]["infile"]
                    mag_ent["_Vu1"] = []
                    mag_ent["_Vu2"] = []
                    mag_ent["_Gii"] = []
                    mag_ent["_MagneticEntity__cell"] = cell
                    mag_ent["_xyz"] = np.array(mag_ent["_xyz"])
                    mag_ent["energies"] = np.array(mag_ent["energies"])
                    mag_ent_list.append(mag_ent)
                    mag_ent = dict()
                    mag_ent["_l"] = []
                    mag_ent["_xyz"] = []
                    mag_ent["energies"] = []
                    continue_writing = None
                    continue

                line = line.split()
                if line[0] == "Tag":
                    mag_ent["_tags"] = line[1:]
                elif line[0] == "Unique":
                    mag_ent["_MagneticEntity__dh_ds_id"] = np.array(
                        [line[2], line[3]], dtype=int
                    )
                    if np.any(
                        mag_ent["_MagneticEntity__dh_ds_id"]
                        != out["hamiltonian"]["_Hamiltonian__dh_ds_id"]
                    ):
                        raise Exception("Inconsistent magnetic entity ID!")
                elif line[0] == "Atom":
                    mag_ent["_atom"] = np.array(line[1:], dtype=int)
                elif line[0] == "Shell":
                    mag_ent["_l"].append(np.array(line[1:], dtype=int))
                    continue_writing = "_l"
                elif line[0] == "Orbital":
                    mag_ent["_orbital_box_indices"] = np.array(line[2:], dtype=int)
                    continue_writing = None
                elif line[0] == "Total":
                    mag_ent["_total_orbital_box_indices"] = np.array(
                        line[3:], dtype=int
                    )
                    continue_writing = None
                elif line[0] == "Position":
                    continue_writing = "_xyz"
                elif line[0] == "Energies":
                    continue_writing = "energies"
                else:
                    if continue_writing == "_l":
                        mag_ent["_l"].append(np.array(line[1:], dtype=int))
                    elif continue_writing == "_xyz":
                        mag_ent["_xyz"].append(np.array(line, dtype=float))
                    elif continue_writing == "energies":
                        mag_ent["energies"].append(np.array(line, dtype=float))
                    else:
                        raise Exception("Bad input file format!")

            if len(mag_ent_list) != NM:
                raise Exception(
                    "Expected number of magnetic entities and read number of magnetic entities are not equal!"
                )
            out["magnetic_entities"] = dict()
            out["magnetic_entities"][
                "_MagneticEntityList__magnetic_entities"
            ] = mag_ent_list
        # pairs
        elif section[0] == "Pairs":
            NP = 0
            if " ".join(section[1].split()[:3]) == "Number of pairs":
                NP = int(section[1].split()[-1])
            pair_list = []
            pair = dict()
            reading_energies = False
            for line in section[3:-1]:
                # new pair
                if line.startswith("----------"):
                    pair["energies"] = np.array(pair["energies"])
                    for m in out["magnetic_entities"][
                        "_MagneticEntityList__magnetic_entities"
                    ]:
                        if "--".join(m["_tags"]) == pair["tags"][0]:
                            pair["M1"] = m
                        if "--".join(m["_tags"]) == pair["tags"][1]:
                            pair["M2"] = m
                    pair["cell"] = cell
                    pair_list.append(pair)
                    pair = dict()
                    reading_energies = False
                # readout
                elif reading_energies:
                    pair["energies"].append(np.array(line.split(), dtype=float))
                else:
                    line = line.split()
                    if line[0] == "Tags":
                        pair["tags"] = line[1:]
                    elif line[0] == "Unique":
                        pair["_Pair__dh_ds_id"] = np.array(
                            [line[2], line[3]], dtype=int
                        )
                        if np.any(
                            pair["_Pair__dh_ds_id"]
                            != out["hamiltonian"]["_Hamiltonian__dh_ds_id"]
                        ):
                            raise Exception("Inconsistent pair ID!")
                    elif line[0] == "Cell":
                        pair["supercell_shift"] = np.array(line[2:5], dtype=int)
                    elif line[0] == "Energies":
                        pair["energies"] = []
                        reading_energies = True

            if len(pair_list) != NP:
                raise Exception(
                    "Expected number of pairs and read number of pairs are not equal!"
                )
            out["pairs"] = dict()
            out["pairs"]["_PairList__pairs"] = pair_list
        # runtimes
        elif section[0] == "Times":
            out["times"] = dict()
            out["times"]["_DefaultTimer__start_measure"] = 0
            out["times"]["_times"] = dict()

            out["hamiltonian"]["times"] = dict()
            out["hamiltonian"]["times"]["_DefaultTimer__start_measure"] = 0
            out["hamiltonian"]["times"]["_times"] = dict()
            out["kspace"]["times"] = dict()
            out["kspace"]["times"]["_DefaultTimer__start_measure"] = 0
            out["kspace"]["times"]["_times"] = dict()
            out["contour"]["times"] = dict()
            out["contour"]["times"]["_DefaultTimer__start_measure"] = 0
            out["contour"]["times"]["_times"] = dict()
            continue_writing = None
            for line in section[1:-1]:
                line = line.split()
                if line[0] == "Builder":
                    continue_writing = "b"
                elif line[0] == "Hamiltonian":
                    continue_writing = "h"
                elif line[0] == "Kspace":
                    continue_writing = "k"
                elif line[0] == "Contour":
                    continue_writing = "c"
                else:
                    if continue_writing == "b":
                        out["times"]["_times"][line[0]] = float(line[1])
                    elif continue_writing == "h":
                        out["hamiltonian"]["times"]["_times"][line[0]] = float(line[1])
                    elif continue_writing == "k":
                        out["kspace"]["times"]["_times"][line[0]] = float(line[1])
                    elif continue_writing == "c":
                        out["contour"]["times"]["_times"][line[0]] = float(line[1])
        elif section[0] == "Mulliken":
            mulliken = []
            for line in section[1:-1]:
                mulliken.append(line.split())
            mulliken = np.array(mulliken, dtype=float).T

    out["_rotated_hamiltonians"] = []
    contour = Contour(
        eset=out["contour"]["_eset"],
        esetp=out["contour"]["_esetp"],
        emin=out["contour"]["_emin"],
        emax=out["contour"]["_emax"],
        emin_shift=0,
        emax_shift=0,
    )
    kspace = Kspace(out["kspace"]["_Kspace__kset"])
    sys = object.__new__(Builder)
    sys.__setstate__(out)
    sys.add_contour(contour)
    sys.add_kspace(kspace)

    for m in sys.magnetic_entities:
        if mulliken is not None:
            m._mulliken = mulliken
        else:
            m._mulliken = None
        m._K = None
        m._K_consistency = None
        if sys.apply_spin_model:
            if sys.spin_model == "generalised-fit":
                m.fit_anisotropy_tensor(sys.ref_xcf_orientations)
            elif sys.spin_model == "generalised-grogu":
                m.calculate_anisotropy()
            else:
                pass

    for p in sys.pairs:
        p._J = None
        if sys.apply_spin_model:
            if sys.spin_model == "generalised-fit":
                p.fit_exchange_tensor(sys.ref_xcf_orientations)
            elif sys.spin_model == "generalised-grogu":
                p.calculate_exchange_tensor()
            elif sys.spin_model == "isotropic-only":
                p.calculate_isotropic_only()
            elif sys.spin_model == "isotropic-biquadratic-only":
                p.calculate_isotropic_biquadratic_only()
            else:
                raise Exception(
                    f"Unknown spin model: {sys.spin_model}! Use apply_spin_model=False"
                )
        for m in sys.magnetic_entities:
            if m.tag == p.M1.tag:
                p.M1 = m
            if m.tag == p.M2.tag:
                p.M2 = m

    return sys


def save_UppASD(
    builder: Builder,
    folder: Union[None, str] = None,
    fast_compare: bool = False,
    spin_moment: str = "total",
    comments: bool = True,
) -> Union[None, list[str]]:
    """Writes the UppASD input files to the given folder.

    The created input files are the posfile, momfile and
    jfile. Furthermore a the inpsd.dat file is created
    with some basic information.

    Parameters
    ----------
    builder : Builder
        Main simulation object containing all the data
    folder : Union[None, str], optional
        The output folder where the files are created or if it is
        set to None, then a list of strings are returned with the
        input data, by default, None
    fast_compare: bool, optional
        When determining the magnetic entity index a fast comparison can
        be used where only the tags are checked, by default False
    spin_moment: str, optional
        It switches the used spin moment in the output, can be 'total'
        for the whole atom or atoms involved in the magnetic entity or
        'local' if we only use the part of the mulliken projections that
        are exactly on the magnetic entity, which may be just a subshell
        of the atom, by default 'total'
    comments: bool, optional
        Wether to add comments in the beginning of the inpsd.dat, by default True

    Returns
    -------
    out: Union[None, str]
        A list of the input file or None, in which case it is written
        to the path
    """

    if builder.apply_spin_model == False:
        raise Exception(
            "Exchange and anisotropy is not calculated! Use apply_spin_model=True"
        )

    posfile = ""
    momfile = ""
    if not builder.spin_model == "isotropic-only":
        # iterating over magnetic entities
        for i, mag_ent in enumerate(builder.magnetic_entities):
            # calculating positions in basis vector coordinates
            bvc = mag_ent.xyz_center @ np.linalg.inv(builder.hamiltonian.cell)
            # adding line to posfile
            posfile += f"{i+1}\t{i+1}\t{bvc[0]:.8f}\t\t{bvc[1]:.8f}\t\t{bvc[2]:.8f}\n"
            # if spin moment is local
            if spin_moment[0].lower() == "l":
                S = np.array([mag_ent.local_Sx, mag_ent.local_Sy, mag_ent.local_Sz])
            # if spin moment is total
            elif spin_moment[0].lower() == "t":
                S = np.array([mag_ent.total_Sx, mag_ent.total_Sy, mag_ent.total_Sz])
            else:
                raise Exception(
                    f"Unrecognized spin moment: {spin_moment}. It can be local or total."
                )

            # get the norm of the vector
            S_abs = np.linalg.norm(S)
            S = S / S_abs
            # adding line to momfile
            momfile += (
                f"{i+1}\t1\t{S_abs:.8f}\t\t{S[0]:.8f}\t\t{S[1]:.8f}\t\t{S[2]:.8f}\n"
            )
    else:
        momfile = "# No on site anisotropy in Isotropic Exchange only mode!"

    jfile = ""
    if not builder.spin_model == "isotropic-only":
        # adding anisotropy to jfile, we need -1, because Uppsala
        # converts it back
        for i, mag_ent in enumerate(builder.magnetic_entities):
            K = -mag_ent.K_mRy.flatten()
            # adding line to jfile
            jfile += (
                f"{i+1}\t{i+1}\t0\t0\t0\t"
                + "\t\t".join(map(lambda x: f"{x:.8f}", K))
                + "\n"
            )

    # iterating over pairs
    for pair in builder.pairs:
        # iterating over magnetic entities and comparing them to the ones stored in the pairs
        for i, mag_ent in enumerate(builder.magnetic_entities):
            if fast_compare:
                if mag_ent.tag == pair.M1.tag:
                    ai = i + 1
                if mag_ent.tag == pair.M2.tag:
                    aj = i + 1
            else:
                if mag_ent == pair.M1:
                    ai = i + 1
                if mag_ent == pair.M2:
                    aj = i + 1

        # this is the unit cell shift
        shift = pair.supercell_shift
        # -1/2 for convention, from uppsala
        J = -1 / 2 * pair.J_mRy.flatten()
        # adding line to jfile
        jfile += (
            f"{ai}\t{aj}\t{shift[0]}\t{shift[1]}\t{shift[2]}\t"
            + "\t\t".join(map(lambda x: f"{x:.8f}", J))
            + "\n"
        )

    # writing them to the given folder
    inpsd = ""
    # if comments are requested
    if comments:
        inpsd += "#" + "\n#".join(str(builder).split("\n"))[:-1]
        inpsd += "\n\n"

    inpsd += "cell " + " \t".join(map(lambda s: f"{s:.8f}", builder.cell[0])) + "\n"
    inpsd += "     " + " \t".join(map(lambda s: f"{s:.8f}", builder.cell[1])) + "\n"
    inpsd += "     " + " \t".join(map(lambda s: f"{s:.8f}", builder.cell[2])) + "\n"
    inpsd += "posfile    ./posfile" + "\n"
    inpsd += "momfile    ./momfile" + "\n"
    inpsd += "exchange   ./jfile" + "\n"
    inpsd += "\n\n"
    inpsd += "do_jtensor 1" + "\n"

    if folder is None:
        return [inpsd, posfile, momfile, jfile]

    with open(join(folder, "inpsd.dat"), "w") as file:
        file.write(inpsd)
    with open(join(folder, "momfile"), "w") as file:
        file.write(momfile)
    with open(join(folder, "posfile"), "w") as file:
        file.write(posfile)
    with open(join(folder, "jfile"), "w") as file:
        file.write(jfile)


def save_Vampire(
    builder: Builder,
    folder: Union[None, str] = None,
    fast_compare: bool = False,
    spin_moment: str = "total",
    comments: bool = True,
) -> Union[None, tuple[str, str, str]]:
    """Writes the Vampire input files to the given folder.

    The main Vampire input file, the .mat and .UCF files
    are created.

    Parameters
    ----------
    builder : Builder
        Main simulation object containing all the data
    folder : Union[None, str], optional
        The output folder where the files are created or if it is
        set to None, then a list of strings are returned with the
        input data, by default, None
    fast_compare: bool, optional
        When determining the magnetic entity index a fast comparison can
        be used where only the tags are checked, by default False
    spin_moment: str, optional
        It switches the used spin moment in the output, can be 'total'
        for the whole atom or atoms involved in the magnetic entity or
        'local' if we only use the part of the mulliken projections that
        are exactly on the magnetic entity, which may be just a subshell
        of the atom, by default 'total'
    comments: bool, optional
        Wether to add comments in the beginning of the input files, by default True

    Returns
    -------
    out: Union[None, tuple[str, str, str]]
        A list of the input files or None, in which case it is written
        to the path
    """

    # ===============================================================
    # Cell transformation
    # ===============================================================
    # number of atoms in the unit cell, number of new layers
    MODULUS = len(builder.magnetic_entities)

    # if it is not a rectangular cell, we try to convert it,
    # but it only works for threefold rotational systems
    normalized_cell = builder.cell / np.linalg.norm(builder.cell, axis=1)
    if not np.isclose(
        np.linalg.norm(
            np.dot(np.cross(normalized_cell[0], normalized_cell[1]), normalized_cell[2])
        ),
        1,
    ):
        if len(builder.magnetic_entities) != 2:
            if PRINTING:
                warnings.warn("Only two magnetic entities in the unit cell is tested!")
        # DIRECTION should be set to 1 or -1 based on the tilt of the paralelogram
        if np.isclose(
            np.dot(normalized_cell[0], normalized_cell[1]),
            -0.5,
        ):
            DIRECTION = -1
        elif np.isclose(
            np.dot(normalized_cell[0], normalized_cell[1]),
            0.5,
        ):
            DIRECTION = 1
        else:
            raise Exception("The unit cell is not threefold rotational symmetric!")

        # test for perpendicular third orientation
        if not np.allclose(normalized_cell[2], np.array([0, 0, 1])):
            raise Exception("The third unit cell vector is not perpendicular!")

    # transform unit cell to rectangle
    a1 = builder.cell[0]
    a2 = np.array([0, np.sqrt(3), 0]) * a1[0]
    a3 = builder.cell[2]
    new_cell = np.array([a1, a2, a3])

    # ===============================================================
    # Generate new magnetic entities
    # ===============================================================
    new_mag_ents = []
    # iterate over magnetic entities
    for i in range(len(builder.magnetic_entities)):
        # iterate over new sublattices
        for j in range(MODULUS):
            m = builder.magnetic_entities[i]

            # calculate relative coordinates
            xyz = m.xyz_center
            # WARNING: this only works for two magnetic entities...
            if j == 1:
                xyz += builder.cell[1]
            # Vampire only accepts relative coordinates between 0 and 1
            # this causes two problems
            # 1 in the original geometry there is a Cr slightly outside the cell
            # 2 the new atomic positions are shifted to one side of the new cell
            # this can be solved by translating and rounding, but this
            # is an ugly solution that works for these atomic positions
            # without having to redefine the unit cell shift indices
            if PRINTING:
                warnings.warn("This is an ugly solution!")
            xyz_rel = np.around(
                np.linalg.inv(new_cell) @ xyz + np.array([0.5, 0, 0]), 4
            )

            # local or total spin moments
            mu = None
            if spin_moment[0].lower() == "l" and m.local_S is not None:
                # because of the Vampire convention, which uses the
                # magnetic moment we need two times the spin moment
                mu = 2 * m.local_S
            elif spin_moment[0].lower() == "t" and m.total_S is not None:
                # because of the Vampire convention, which uses the
                # magnetic moment we need two times the spin moment
                mu = 2 * m.total_S
            else:
                raise Exception(
                    f"Unrecognized spin moment: {spin_moment}. It can be local or total."
                )

            new_mag_ents.append(
                dict(
                    idx=i,  # original magnetic entity index
                    tag=m.tag,  # tag
                    spin_moment=mu,  # magnetic moment
                    new_idx=MODULUS * i + j,  # new magnetic entity index
                    relative_coordinates=xyz_rel,  # relative atomic coordinates
                )
            )

    # ===============================================================
    # Generate new pairs
    # ===============================================================
    new_pairs = []
    # iterate over pairs
    for i in range(len(builder.pairs)):
        # iterate over new sublattices
        for j in range(MODULUS):
            p = builder.pairs[i]

            # iterating over magnetic entities and comparing them to the ones stored in the pairs
            m1_idx = None
            m2_idx = None
            for k, mag_ent in enumerate(builder.magnetic_entities):
                if fast_compare:
                    if mag_ent.tag == p.M1.tag:
                        m1_idx = k
                    if mag_ent.tag == p.M2.tag:
                        m2_idx = k
                else:
                    if mag_ent == p.M1:
                        m1_idx = k
                    if mag_ent == p.M2:
                        m2_idx = k
            if m1_idx is None or m2_idx is None:
                raise Exception("Magnetic entities not found!")

            # unit cell shift of the pair
            shift1 = p.supercell_shift[0]
            shift2 = p.supercell_shift[1]
            shift3 = p.supercell_shift[2]

            # new indices and unit cell shifts
            new_pairs.append(
                dict(
                    m1=MODULUS * m1_idx + j,
                    m2=MODULUS * m2_idx
                    + (j + (shift2 % MODULUS + MODULUS) % MODULUS) % MODULUS,
                    uc_shift=[
                        shift1
                        + DIRECTION
                        * ((shift2 - (shift2 % MODULUS + MODULUS) % MODULUS) // MODULUS)
                        + DIRECTION
                        * ((j + (shift2 % MODULUS + MODULUS) % MODULUS) // MODULUS),
                        (shift2 - (shift2 % MODULUS + MODULUS) % MODULUS) // MODULUS
                        + (j + (shift2 % MODULUS + MODULUS) % MODULUS) // MODULUS,
                        shift3,
                    ],
                    # corresponding exchange in Joule
                    # and convention change (Vampire does not have 1/2,
                    # but it sums only on half of the pairs)
                    J=-1 * builder.pairs[i].J_J.flatten(),
                )
            )

    # ===============================================================
    # Write Vampire input files
    # ===============================================================
    # Vampire main input file
    inp = ""
    if comments:
        inp += "#" + "\n#".join(str(builder).split("\n"))[:-1]
        inp += "\n\n"
    inp += "#------------------------------------------\n"
    inp += "# Grogupy generated Vampire input file to \n"
    inp += "# perform Curie temperature calculation\n"
    inp += "#------------------------------------------\n"
    inp += "material:file =           vampire.mat\n"
    inp += "material:unit-cell-file = vampire.UCF\n"
    inp += "#------------------------------------------\n"
    inp += "# Creation attributes:\n"
    inp += "#------------------------------------------\n"
    inp += "dimensions:system-size-x = 50 !nm\n"
    inp += "dimensions:system-size-y = 50 !nm\n"
    # if the system is 2D and not bulk
    if np.allclose(builder.pairs.supercell_shift[:, 2], 0):
        # divide by 10 to convert Ang to nm
        # constrain system size to less than a unit cell to get a single layer
        inp += f"dimensions:system-size-z = {np.linalg.norm(new_cell[2]) * 0.99 / 10} !nm\n"
    # if it is bulk use the same size as x and y
    else:
        inp += "dimensions:system-size-z = 50 !nm\n"
    inp += "#------------------------------------------\n"
    inp += "# Simulation attributes:\n"
    inp += "#------------------------------------------\n"
    inp += "sim:minimum-temperature = 0.0\n"
    inp += "sim:maximum-temperature = 200.0\n"
    inp += "sim:temperature-increment = 0.5\n"
    inp += "sim:loop-time-steps = 5000.0\n"
    inp += "sim:equilibration-time-steps = 10000.0\n"
    inp += "sim:time-step = 0.1 !fs\n"
    inp += "#------------------------------------------\n"
    inp += "# Program and integrator details\n"
    inp += "#------------------------------------------\n"
    inp += "sim:program = curie-temperature\n"
    inp += "sim:integrator = monte-carlo # or llg-heun for spin dinamics\n"
    inp += "#------------------------------------------\n"
    inp += "# Data output\n"
    inp += "#------------------------------------------\n"
    inp += "output:real-time\n"
    inp += "output:temperature\n"
    inp += "output:magnetisation\n"
    inp += "output:mean-susceptibility\n"
    inp += "screen:temperature\n"
    inp += "screen:magnetisation\n"

    # Vampire material file
    mat = (
        f"material:num-materials = {len(np.unique([m['tag'] for m in new_mag_ents]))}\n"
    )
    mat += "#---------------------------------------------------\n"
    unique = []
    for i in range(len(new_mag_ents)):
        if new_mag_ents[i]["tag"] not in unique:
            mat += "\n"
            mat += f"# Material {new_mag_ents[i]['idx']+1}\n"
            mat += f"material[{new_mag_ents[i]['idx']+1}]:material-name = {new_mag_ents[i]['tag'].replace(':', '_')}\n"
            mat += f"material[{new_mag_ents[i]['idx']+1}]:material-element = "
            mat += f"{''.join([i for i in new_mag_ents[i]['tag'].split('(')[0] if not i.isdigit()])}\n"
            mat += f"material[{new_mag_ents[i]['idx']+1}]:unit-cell-category = {new_mag_ents[i]['idx']+1}\n"
            mat += f"material[{new_mag_ents[i]['idx']+1}]:atomic-spin-moment = {new_mag_ents[i]['spin_moment']} ! muB\n"
            mat += f"material[{new_mag_ents[i]['idx']+1}]:initial-spin-direction = 0, 0, 1\n"
            mat += f"material[{new_mag_ents[i]['idx']+1}]:damping-constant = 0.1\n"

            ################################################################################
            # Calculate on-site anisotropy in Vampire format
            ################################################################################
            # convert to Joule from eV
            eigs, eigvecs = np.linalg.eig(
                builder.magnetic_entities[new_mag_ents[i]["idx"]].K_J
            )

            # we iterate over a range of possible roundings to find the unique eigenvalue
            # (we could take the minimum, but that does not neccesarily work for easy plane)
            easy_idx = None
            for r in range(40):
                # round eigenvalues
                reigs = np.around(eigs, r)
                # if there are two unique eigenvalues we can get the easy axis,
                # else continue
                if len(np.unique(reigs)) == 2:
                    # if the eigenvalues contains the first unique eigenvalue only once,
                    # then it is the easy axis index
                    if (np.unique(reigs)[0] == reigs).sum() == 1:
                        easy_idx = np.where(np.unique(reigs)[0] == reigs)[0][0]
                        plane_idx = np.where(np.unique(reigs)[1] == reigs)[0]
                        # calculate the anisotropy constant from the easy axis and hard plane difference
                        anisotropy_constant = eigs[plane_idx].mean() - abs(
                            eigs[easy_idx]
                        )
                    # else the second unique eigenvalue is the easy axis
                    else:
                        easy_idx = np.where(np.unique(reigs)[1] == reigs)[0][0]
                        plane_idx = np.where(np.unique(reigs)[0] == reigs)[0]
                        # calculate the anisotropy constant from the easy axis and hard plane difference
                        anisotropy_constant = eigs[plane_idx].mean() - abs(
                            eigs[easy_idx]
                        )
                    break
            # if there is no unique eigenvalue
            if easy_idx is None:
                print(eigs)
                raise Exception("Easy axis not found!")

            mat += f"material[{new_mag_ents[i]['idx']+1}]:uniaxial-anisotropy-constant = {anisotropy_constant}\n"
            mat += (
                f"material[{new_mag_ents[i]['idx']+1}]:uniaxial-anisotropy-direction = "
            )
            mat += ", ".join(map(lambda x: f"{x:.6e}", eigvecs[:, easy_idx]))
            mat += "\n"
            mat += "#---------------------------------------------------\n"
            unique.append(new_mag_ents[i]["tag"])

    # Vampire unit cell file
    ucf = ""
    ucf += "# Unit cell size:\n"
    ucf += "\t".join(map(lambda x: f"{x:.8f}", np.linalg.norm(new_cell, axis=1))) + "\n"
    # this is not used by Vampire, just fake cell vectors...
    ucf += "# Unit cell lattice vectors:\n"
    ucf += "1.0 0.0 0.0\n"
    ucf += "0.0 1.0 0.0\n"
    ucf += "0.0 0.0 1.0\n"
    ucf += "# Atoms\n"
    ucf += f"{len(new_mag_ents)}\t{len(new_mag_ents)}\n"
    for i in range(len(new_mag_ents)):
        ucf += f"{i}\t"
        ucf += "\t".join(
            map(lambda x: f"{x:.8f}", new_mag_ents[i]["relative_coordinates"])
        )
        ucf += f"\t{new_mag_ents[i]['idx']}"
        ucf += f"\t{i+1}"
        ucf += "\t0"
        ucf += "\n"
    ucf += "# Interactions\n"
    ucf += f"{len(new_pairs)} tensorial\n"
    for i in range(len(new_pairs)):
        ucf += f"{i}\t"
        ucf += f"{new_pairs[i]['m1']}\t{new_pairs[i]['m2']}\t"
        ucf += "\t".join(map(lambda x: f"{x:d}", new_pairs[i]["uc_shift"]))
        ucf += "\t"
        ucf += "\t".join(map(lambda x: f"{x:.6e}", new_pairs[i]["J"]))
        ucf += "\n"

    # if the output folder was not given return the files as string
    if folder is None:
        return inp, mat, ucf
    # else create the files in the folder
    else:
        with open(join(folder, "input"), "w") as file:
            file.write(inp)
        with open(join(folder, "vampire.mat"), "w") as file:
            file.write(mat)
        with open(join(folder, "vampire.UCF"), "w") as file:
            file.write(ucf)


def save_magnopy(
    builder: Builder,
    path: Union[None, str] = None,
    spin_moment: str = "total",
    comments: bool = True,
) -> Union[None, str]:
    """Creates a magnopy input file.

    Parameters
    ----------
    builder: Builder
        The system that we want to save
    path: Union[None, str], optional
        Output path or if None it returns a string, by default None
    spin_moment: str, optional
        It switches the used spin moment in the output, can be 'total'
        for the whole atom or atoms involved in the magnetic entity or
        'local' if we only use the part of the mulliken projections that
        are exactly on the magnetic entity, which may be just a subshell
        of the atom, by default 'total'
    comments: bool, optional
        Wether to add comments in the beginning of file, by default True

    Returns
    -------
    out: Union[None, str]
        A string of the input file or None, in which case it is written
        to the path
    """

    if path is not None:
        if not path.endswith(".magnopy.txt"):
            path += ".magnopy.txt"

    if builder.apply_spin_model == False:
        raise Exception(
            "Exchange and anisotropy is not calculated! Use apply_spin_model=True"
        )

    section = "================================================================================"
    subsection = "--------------------------------------------------------------------------------"
    newline = "\n"

    out = ""
    out += section + newline
    out += "GROGU INFORMATION" + newline
    if comments:
        out += newline
        out += "#" + "\n#".join(str(builder).split("\n"))[:-1]
        out += newline + newline

    out += section + newline
    out += "Hamiltonian convention" + newline
    out += "Double counting      true" + newline
    out += "Normalized spins     true" + newline
    out += "Intra-atomic factor  +1" + newline
    out += "Exchange factor      +0.5" + newline

    out += section + newline
    out += f"Cell (Ang)" + newline
    if builder.cell is not None:
        out += "\t".join(map(lambda s: f"{s:.8f}", builder.cell[0])) + newline
        out += "\t".join(map(lambda s: f"{s:.8f}", builder.cell[1])) + newline
        out += "\t".join(map(lambda s: f"{s:.8f}", builder.cell[2])) + newline
    else:
        raise Exception("Cell is not defined!")

    out += section + newline
    out += "Magnetic sites" + newline
    out += f"Number of sites {len(builder.magnetic_entities)}" + newline
    out += (
        "Name\t\tx (Ang)\t\ty (Ang)\t\tz (Ang)\t\ts\t\t\tsx\t\t\tsy\t\t\tsz" + newline
    )
    for mag_ent in builder.magnetic_entities:
        out += mag_ent.tag + "\t"
        out += "\t".join(map(lambda s: f"{s:.8f}", mag_ent._xyz.mean(axis=0)))
        out += "\t"
        if spin_moment[0].lower() == "l":
            s = np.array([mag_ent.local_Sx, mag_ent.local_Sy, mag_ent.local_Sz])
            if s[0] is not None:
                s = s / np.linalg.norm(s)
                out += f"{mag_ent.local_S:.8f}\t{s[0]:.8f}\t{s[1]:.8f}\t{s[2]:.8f}"
            else:
                out += "None\tNone\tNone\tNone"
        elif spin_moment[0].lower() == "t":
            s = np.array([mag_ent.total_Sx, mag_ent.total_Sy, mag_ent.total_Sz])
            if s[0] is not None:
                s = s / np.linalg.norm(s)
                out += f"{mag_ent.total_S:.8f}\t{s[0]:.8f}\t{s[1]:.8f}\t{s[2]:.8f}"
            else:
                out += "None\tNone\tNone\tNone"
        else:
            raise Exception(
                f"Unrecognized spin moment: {spin_moment}. It can be local or total."
            )
        out += newline

    out += section + newline
    out += "Intra-atomic anisotropy tensor (meV)" + newline
    for mag_ent in builder.magnetic_entities:
        out += subsection + newline
        out += mag_ent.tag + newline
        if mag_ent.K_meV is not None:
            K = mag_ent.K_meV
        else:
            K = np.zeros((3, 3))
        out += "Matrix" + newline
        out += "\t" + "\t".join(map(lambda s: f"{s:.8f}", K[0])) + newline
        out += "\t" + "\t".join(map(lambda s: f"{s:.8f}", K[1])) + newline
        out += "\t" + "\t".join(map(lambda s: f"{s:.8f}", K[2])) + newline
    out += subsection + newline

    out += section + newline
    out += "Exchange tensor (meV)" + newline
    out += f"Number of pairs {len(builder.pairs)}" + newline
    out += subsection + newline
    out += "Name1\t\tName2\t\ti\tj\tk\td (Ang)" + newline
    for pair in builder.pairs:
        out += subsection + newline
        tag = pair.tags[0] + "\t" + pair.tags[1]
        out += tag + "\t" + "\t".join(map(str, pair.supercell_shift))
        out += f"\t{pair.distance}" + newline
        if pair.J_meV is not None:
            J = pair.J_meV
        else:
            raise Exception("J is None!")
        out += "Matrix" + newline
        out += "\t" + "\t".join(map(lambda s: f"{s:.8f}", J[0])) + newline
        out += "\t" + "\t".join(map(lambda s: f"{s:.8f}", J[1])) + newline
        out += "\t" + "\t".join(map(lambda s: f"{s:.8f}", J[2])) + newline
    out += subsection + newline
    out += section + newline

    if path is None:
        return out

    with open(path, "w") as file:
        file.write(out)


def save_HDF5(
    builder: Builder,
    path: str,
) -> None:
    """Creates a HDF5 output file.

    Parameters
    ----------
    builder: Builder
        The system that we want to save
    path: str
        Output path
    """

    if not path.endswith(".hdf5"):
        path += ".hdf5"
    file = h5py.File(path, "w")

    # Metadata
    metadata = file.create_group("Metadata")
    metadata.create_dataset("Version", data=builder.version)
    metadata.create_dataset("Architecture", data=builder.architecture)
    metadata.create_dataset("SLURM job ID", data=builder.SLURM_ID)
    metadata.create_dataset("Input file", data=builder.infile)
    # Hamiltonian
    hamiltonian = file.create_group("Hamiltonian")
    hamiltonian.create_dataset("Spin model", data=builder.spin_model)
    if builder.hamiltonian is not None:
        hamiltonian.create_dataset("Spin mode", data=builder.hamiltonian._spin_state)
        hamiltonian.create_dataset("Number of orbitals", data=builder.hamiltonian.NO)
    else:
        hamiltonian.create_dataset("Spin mode", data="Not defined")
        hamiltonian.create_dataset("Number of orbitals", data="Not defined")
    # Solver
    solver = file.create_group("Solver")
    if builder.architecture == "CPU":
        solver.create_dataset(
            "Number of threads in the parallel cluster", data=CONFIG.parallel_size
        )
    elif builder.architecture == "GPU":
        solver.create_dataset(
            "Number of GPUs in the cluster", data=CONFIG.parallel_size
        )
    else:
        raise Exception(f"Unknown architecture: {builder.architecture}")
    if builder.parallel_mode is None:
        solver.create_dataset("Parallelization is over", data="No parallelization")
    else:
        solver.create_dataset("Parallelization is over", data=builder.parallel_mode)
    solver.create_dataset(
        "Solver used for Greens function calculation",
        data=builder.greens_function_solver,
    )
    if builder.greens_function_solver[0].lower() == "s":
        max_g = builder.__max_g_per_loop
    else:
        if builder.contour is not None:
            max_g = builder.contour.eset
        else:
            max_g = "Not defined"
    solver.create_dataset(
        "Maximum number of Greens function samples per batch", data=max_g
    )
    # Cell [Ang]
    file.create_dataset("Cell [Ang]", data=builder.cell)
    # Exchange field rotations
    xcf = file.create_group("Exchange field rotations")
    xcf.create_dataset("DFT axis", data=builder.scf_xcf_orientation)
    rotations = xcf.create_group("Quantization axis and perpendicular directions")
    for i, ref in enumerate(builder.ref_xcf_orientations):
        r = rotations.create_group(str(i))
        r.create_dataset("o", data=ref["o"])
        r.create_dataset("vw", data=ref["vw"])
    # Kspace
    kspace = file.create_group("Kspace")
    kspace.create_dataset("Nkpoints", data=builder.kspace.NK, dtype="i")
    kspace.create_dataset("Kset", data=builder.kspace.kset, dtype="i")
    # Contour
    contour = file.create_group("Contour")
    contour.create_dataset("Eset", data=builder.contour.eset, dtype="i")
    contour.create_dataset("Esetp", data=builder.contour.esetp, dtype="i")
    contour.create_dataset("Ebot", data=builder.contour.emin)
    contour.create_dataset("Etop", data=builder.contour.emax)
    # Magnetic entities
    magnetic_entities = file.create_group("Magnetic entities")
    for i, mag_ent in enumerate(builder.magnetic_entities):
        m = magnetic_entities.create_group(str(i))
        m.create_dataset("Tag", data=mag_ent.tag)
        m.create_dataset("Atom", data=mag_ent._atom, dtype="i")
        m.create_dataset("Shell", data=mag_ent._l, dtype="i")
        m.create_dataset("Orbital box", data=mag_ent._orbital_box_indices, dtype="i")
        m.create_dataset("Position [Ang]", data=mag_ent._xyz)
        m.create_dataset("Energies [eV]", data=mag_ent.energies)
    # Pairs
    pairs = file.create_group("Pairs")
    for i, pair in enumerate(builder.pairs):
        p = pairs.create_group(str(i))
        p.create_dataset("Tag", data=pair.tags)
        p.create_dataset("Supercell shift", data=pair.supercell_shift, dtype="i")
        p.create_dataset("Energies [eV]", data=pair.energies, dtype="i")
    # Mullikens
    mismatch = False
    base = builder.magnetic_entities[0]
    for m in builder.magnetic_entities:
        if m._mulliken is None and base._mulliken is None:
            pass
        else:
            if not arrays_lists_equal(m._mulliken, base._mulliken):
                mismatch = True
                break
    if not mismatch and base._mulliken is not None:
        file.create_dataset("Mulliken", data=base._mulliken)

    file.close()


def read_fdf(path: str) -> dict:
    """It reads the simulation parameters, magnetic entities and pairs from an fdf file.

    Parameters
    ----------
        path: str
            The path to the .fdf file

    Returns
    -------
        out: dict
            The input parameters
    """

    out = dict()
    with open(path) as f:
        while True:
            # preprocess
            line = f.readline()
            if not line:
                break
            line = line[: line.find("#")]
            if len(line.strip()) != 0:
                line = line.split()
                line[0] = line[0].replace("_", "").replace(".", "").lower()

                # these are blocks
                if line[0].lower() == r"%block":
                    # name so we can choose process function
                    name = line[1].replace("_", "").replace(".", "").lower()

                    # iterate over lines and get preprocessed data
                    lines = []
                    while True:
                        # preprocess
                        line = f.readline()
                        # if endblock break loop
                        if line.split()[0].lower() == r"%endblock":
                            break
                        if not line:
                            raise Exception(f"End of file in block: {name}")
                        line = line[: line.find("#")]
                        if len(line.strip()) != 0:
                            lines.append(line)

                    if name == "refxcforientations":
                        out_lines = []
                        for l in lines:
                            l = l.split()
                            # we expected either 3 numbers of reference direction or
                            # some number of perpendicular directions which is defined
                            # by 3 numbers as well
                            if len(l) % 3 != 0:
                                raise Exception(
                                    "Some number of 3D vectors are expected."
                                )
                            # check if the row is integer or not
                            just_int = True
                            for v in l:
                                if not v.isdigit():
                                    just_int = False
                            # if the perpendicular directions are not given
                            if len(l) == 3:
                                if just_int:
                                    out_lines.append(list(map(int, l)))
                                else:
                                    out_lines.append(list(map(float, l)))
                            # if it is an input dictionary format
                            else:
                                if just_int:
                                    l = list(map(int, l))
                                else:
                                    l = list(map(float, l))
                                out_ref = {"o": [], "vw": []}
                                # iterate over the vectors
                                for i in range(len(l) // 3):
                                    if i == 0:
                                        out_ref["o"] = l[i * 3 : i * 3 + 3]
                                    else:
                                        out_ref["vw"].append(l[i * 3 : i * 3 + 3])
                                out_lines.append(out_ref)

                    elif name == "magneticentities":
                        out_lines = []
                        for l in lines:
                            l = l.split()
                            if l[0].lower() == "orbitals":
                                out_lines.append(dict(orb=list(map(int, l[1:]))))
                            elif l[0].lower() == "cluster":
                                out_lines.append(dict(atom=list(map(int, l[1:]))))
                            elif l[0].lower() == "atom":
                                if len(l) != 2:
                                    raise Exception("Atom should be a single atom!")
                                else:
                                    out_lines.append(dict(atom=int(l[1])))
                            elif l[0].lower() == "atomshell":
                                out_lines.append(
                                    dict(atom=int(l[1]), l=list(map(int, l[2:])))
                                )
                            elif l[0].lower() == "atomorbital":
                                out_lines.append(
                                    dict(atom=int(l[1]), orb=list(map(int, l[2:])))
                                )
                            else:
                                raise Exception("Unknown magnetic entity!")

                    elif name == "pairs":
                        out_lines = []
                        for l in lines:
                            l = l.split()
                            out_lines.append(
                                dict(
                                    ai=int(l[0]),
                                    aj=int(l[1]),
                                    Ruc=list(map(int, l[2:5])),
                                )
                            )
                            # this is special, because we have to set up a dict from a single line
                    elif name == "kwargsformagent":
                        out_lines = dict()
                        for l in lines:
                            l = l.split()
                            if l[0].lower() == "l":
                                out_lines["l"] = list(map(int, l[1:]))
                            elif l[0].lower() == "o":
                                out_lines["orb"] = list(map(int, l[1:]))
                            else:
                                if l[1].lower() == "l":
                                    out_lines[l[0]]["l"] = list(map(int, l[2:]))
                                elif l[1].lower() == "o":
                                    out_lines[l[0]]["orb"] = list(map(int, l[2:]))
                                else:
                                    raise Exception(
                                        f"Unknown kwarg for magnetic entities: {l[0]}!"
                                    )
                    else:
                        pass
                    out[name] = out_lines

                # these are single line lists
                elif len(line) > 2:
                    just_int = True
                    for l in line[1:]:
                        if not l.isdigit():
                            just_int = False
                    if just_int:
                        out[line[0]] = list(map(int, line[1:]))
                    else:
                        out[line[0]] = list(map(float, line[1:]))

                # one keyword stuff
                elif len(line) == 2:
                    # check for integers
                    if line[1].isdigit():
                        out[line[0]] = int(line[1])
                    else:
                        # else try floats and continue if it works
                        try:
                            out[line[0]] = float(line[1])
                            continue
                        except:
                            pass
                        # the rest are strings, none or bool
                        if line[1].lower() == "none":
                            out[line[0]] = None
                        elif line[1].lower() == "true":
                            out[line[0]] = True
                        elif line[1].lower() == "false":
                            out[line[0]] = False
                        else:
                            out[line[0]] = line[1]
    return out


def read_py(path: str) -> dict:
    """Reading input parameters from a .py file.

    Parameters
    ----------
    path: str
        The path to the input file

    Returns
    -------
    out : dict
        The input parameters
    """

    # Create the spec
    spec = importlib.util.spec_from_file_location("grogupy_command_line_input", path)

    # Create the module
    if spec is not None:
        params = importlib.util.module_from_spec(spec)
        loader = spec.loader
        if loader is not None:
            loader.exec_module(params)
        else:
            raise Exception("File could not be loaded!")

    else:
        raise Exception("File could not be loaded!")

    # convert to dictionary
    out = dict()
    for name in params.__dir__():
        if not name.startswith("__") or name == "np" or name == "numpy":
            n = name.replace("_", "").replace(".", "").lower()
            out[n] = params.__dict__[name]

    return out


if __name__ == "__main__":
    pass
