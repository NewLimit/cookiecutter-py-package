.ONESHELL:

SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

# Constants
CONFIG_DIR="/efs/home/conner/src/nlmt_cookiecutter/{{ cookiecutter.project_slug }}/{{ cookiecutter.python_slug }}/analysis/00000000_example_analysis/config"
CONDA_ENV=/efs/home/conner/conda/envs/scg_tools # TODO: Update conda env path

# Targets
01_submitit_hydra_example:
	${CONDA_ACTIVATE} ${CONDA_ENV}
	nohup python steps/01_submitit_hydra_example.py \
		--config-path=${CONFIG_DIR} \
		--config-name=01_submitit_hydra_example \
		> logs/01_submitit_hydra_example.log 2>&1 &

02_papermill_example:
	${CONDA_ACTIVATE} ${CONDA_ENV}
	papermill steps/02_papermill_example.ipynb \
		logs/02_papermill_example.ipynb \
		-f ${CONFIG_DIR}/02_papermill_example.yaml

