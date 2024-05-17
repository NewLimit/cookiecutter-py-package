# Example directory strcuture and scripts for an analysis

CSK, 2024-05-17

## Overview

This directory contains an example scripts for an analysis. The code for each step in the analysis lives in the `./steps` directory and the parameters used for each step live in a config in the `./config` directory. Each step is run using the provided `Makefile`.

## Background

Provide relavant background information about the analysis and/or links to relevant documentation such as Notion pages.

## Steps

1. `01_submitit_hydra_example`: A simple example of how to use `submitit` and `hydra` to run python code on a SLURM cluster.
2. `02_papermill_example`: A simple example of how to use `papermill` to run a juptyer notebook from the CLI in a reproducible way.
