# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - yyyy-mm-dd





## [0.4.0] - 2025-10-27

### Added

- save_grogupy with energy format instead of spin model.
- On-site anisotropy tensor plotter.
- Unique ID based on the Hamiltonian and the density matrix.
- Representation and string format to ``DefaultTimer``.
- Added plot_J_S_distance function.
- Grouping options of pairs on distance plots.
- New plotting functions to analysis command line tool.
- Experimental anisotropy fitting, this have to be tested.
- Input file generator for convergence tests.
- Low memory mode information to printing.
- Dependecy graph.
- Magnetic entity and pair generation tutorial to the documentation.

### Changed

- Changed magnetic moment to spin moment.
- Removed precision setting in output files.
- Changed cell.tmp.txt to inpsd.dat in Uppsala output and filled with default values.
- Input file is stored as absoluth path in ``Hamiltonian``.
- Internal changes.
- openmpi is optional dependency.
- Using h5py instead of netcdf4.
- Some printing formats in the output files.
- Standardized plotly colors.
- ``MagneticEntityList`` and ``PairList`` properties are type hinted.
- Using Literals on string inputs.

### Fixed

- Cleaner documentation.
- Hamiltonian convention in Uppsala, Vampire and magnopy output.
- Vampire cell transforamtion for C3 symmetric systems.
- ``MagneticEntityList`` and ``PairList`` indexing.
- Citation.
- Sometimes in the isotropic-only spin model case reference directions werent set correctly.
- Symmetric traceless exchange was not traceless.
- ``MagneticEntity`` creation with different number of orbitals.
- Normalizing ``scf_orientation``.
- Save and load functions (they are still version dependent).
- Fixed ``plot_1D_convergence`` function.
- Fixed ``grogupy_convergence`` command line tool.





## [0.3.1] - 2025-07-22

### Added

- Vampire input generation.
- Cell propery to Builder.
- Default values to Contour.

### Changed

- Improve user information for memory allocation.
- Nicer printing in Builder.
- Nicer printing in magnopy input.
- Many class variables became properties.

### Fixed

- Failed tqdm loading prints error message only once through MPI.
- Using spin moment instead of magnetic moment to follow magnopy convention.
- *.fdf* input is not enforced in the command line tool.
