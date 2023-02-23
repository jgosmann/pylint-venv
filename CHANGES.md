# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.1] - 2023-02-23

### Fixed

- Add changelog (`CHANGES.md`) back into source distribution.


## [3.0.0] - 2023-02-22

### Changed

- Require that the `force_venv_activation` argument to `inithook` is passed
  as keyword argument.
  
### Removed

- Remove (official) support for Python 3.6.

### Fixed

- Do not include documentation files in pure library distribution
  ([#13](https://github.com/jgosmann/pylint-venv/pull/13)).
- Clarify that the hook has to be configured in the `[MAIN]` section
  ([#14](https://github.com/jgosmann/pylint-venv/pull/14))


## [2.3.0] - 2022-06-24

### Added

- Add `quiet` argument to `inithook` method. It suppresses all output from the
  plugin.

## [2.2.0] - 2022-06-07

### Added

- Check alternative directory locations given by the `PYLINT_VENV_PATH`
  environment variable. The variable consists of paths separated by a
  colon `:`.

## [2.1.1] - 2020-08-17

### Fixed

- Activate virtual environment even if its Python version does not match the
  Python version used by pylint. Note that Python packages in the virtual
  environment incombatible with pylint's Python version will not work.

## [2.1.0] - 2020-03-22

### Added

- Support for using pylint installed in a virtual environment.
  See `force_venv_activation` parameter on `inithook` method.

## [2.0.0] - 2019-10-19

### Added

- Support for Conda and PyPy
- Documentation improvements

### Removed

- Support for Python 2.7.

## [1.1.0] - 2019-03-26

### Added

- Compatibility with Python 3 venv module.

## [1.0.0] - 2015-03-01

### Added

- Initial release of inithook for pylint to activate virtual env.

[unreleased]: https://github.com/jgosmann/pylint-venv/compare/v3.0.1...HEAD
[3.0.1]: https://github.com/jgosmann/pylint-venv/compare/v3.0.0...v3.0.1
[3.0.0]: https://github.com/jgosmann/pylint-venv/compare/v2.3.0...v3.0.0
[2.3.0]: https://github.com/jgosmann/pylint-venv/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/jgosmann/pylint-venv/compare/v2.1.0...v2.2.0
[2.1.1]: https://github.com/jgosmann/pylint-venv/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/jgosmann/pylint-venv/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/jgosmann/pylint-venv/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/jgosmann/pylint-venv/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/jgosmann/pylint-venv/releases/tag/v1.0.0
