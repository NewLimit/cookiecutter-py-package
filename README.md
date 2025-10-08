# Cookiecutter Py Package

[![Build Status](https://github.com/evamaxfield/cookiecutter-py-package/workflows/CI/badge.svg)](https://github.com/evamaxfield/cookiecutter-py-package/actions)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Yet another Cookiecutter template for a Python package.

## About

`Cookiecutter` is a Python package to generate templated projects.
This repository is a template for `cookiecutter` to generate a Python project which
contains following:

-   A directory structure for your project
-   Prebuilt `pyproject.toml` file to help you develop and install your package
-   Includes basic examples of modules, tests, bin scripts, etc.
-   Continuous integration
    -   Preconfigured to generate project documentation (library packages)
    -   Preconfigured to automatically run tests every time you push to GitHub
-   **Two package types:**
    -   **Analysis**: Lightweight template for data analysis projects with numpy, pandas, matplotlib, jupyter, and jupytext pre-configured. Minimal documentation overhead.
    -   **Library**: Full-featured template for distributable Python libraries with Sphinx documentation, check-manifest, and CLI entry points.

We think that this template provides a good starting point for any Python project.

## Quickstart

To use this template use the following commands.

1. `pip install cookiecutter`
2. `cookiecutter gh:NewLimit/cookiecutter-py-package`

Once the project is generated, move to the newly created project directory
and follow the instructions in `SETUP.md`.

### Package Types

When prompted, choose the package type that fits your needs:

-   **analysis**: For data analysis projects, research code, and exploratory work
    -   Includes: numpy, pandas, matplotlib, seaborn, jupyter, jupytext, papermill
    -   Excludes: Sphinx docs, check-manifest, CLI entry points
    -   Minimal linting (no docstring requirements)
    -   Includes helpful just commands: `sync-notebooks`, `run-notebook`
    -   `.gitignore` configured for data files (`.h5ad`, `.parquet`, `.zarr`, etc.)

-   **library**: For distributable Python packages and libraries
    -   Includes: Sphinx documentation, check-manifest
    -   Includes: CLI entry point examples
    -   Comprehensive linting with docstring requirements
    -   Includes just commands: `generate-docs`, `serve-docs`

### Notes

1. Requires Python `>=3.10` and `setuptools>=64.0` to install library locally in editable mode
    * Most environment managers pull in the latest `setuptools` automatically when
      creating a new environment anyway.
2. Must initialize the project as a `git` repository prior to installing locally.
    * This is due to the dynamic version management with `setuptools-scm`.
    * After running the cookiecutter, you should push code to a remote host
      (GitHub, GitLab, etc.) or at the very least, run `git init` prior to install.
3. It is generally recommended to use VSCode and install the extensions for
    ruff and pre-commit.

## Features

-   Uses `pytest` for local testing, simply run `just build` from a terminal.
-   Runs tests on Python 3.10, 3.11, and 3.12 on every commit to `main` and
    every commit to branches with an open `pull request` to `main` using GitHub Actions.
-   Uses `uv` for fast dependency installation in CI.
-   Uses `ruff` for linting and formatting.
-   Uses `just` for task automation (like `make` but better).
-   Includes very minimal example code to get started.

### Library Package Features
-   Automatically builds documentation using Sphinx.
-   Uses `check-manifest` to ensure package contents are correct.
-   Includes CLI entry point examples.

### Analysis Package Features
-   Pre-configured with numpy, pandas, matplotlib, seaborn.
-   Includes jupyter, jupytext for notebook-based workflows.
-   Includes papermill for reproducible notebook execution.
-   `.gitignore` configured for common data science files.
-   Lenient linting (no docstring requirements for analysis code).

List of available [just](https://github.com/casey/just) commands:
```bash
just
```
Common commands for all packages:
```
Available recipes:
    build                    # run lint and then run tests
    clean                    # clean all build, python, and lint files
    default                  # list all available commands
    install                  # install with all deps
    lint                     # lint, format, and check all files
    tag-for-release version  # tag a new version
    release                  # release a new version
    test                     # run tests
    update-from-cookiecutter # update this repo using latest cookiecutter-py-package
```

Additional commands for **library** packages:
```
    generate-docs            # generate Sphinx HTML documentation
    serve-docs               # generate Sphinx HTML documentation and serve to browser
```

Additional commands for **analysis** packages:
```
    sync-notebooks           # convert notebooks to paired .py files for version control
    run-notebook             # run a notebook with papermill
```
