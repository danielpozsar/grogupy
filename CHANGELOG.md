# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - yyyy-mm-dd


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
- .fdf input is not enforced in the command line tool.
