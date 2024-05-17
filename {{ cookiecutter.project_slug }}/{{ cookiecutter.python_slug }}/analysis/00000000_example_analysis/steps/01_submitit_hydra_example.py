"""Example script for kicking off a job with submitit and hydra."""


import logging
from pathlib import Path

import hydra
import submitit
from omegaconf import DictConfig, OmegaConf

logger = logging.getLogger(__name__)


def simple_function(x: int) -> int:
    """Simple function that adds 1 to an integer."""
    return x + 1


@hydra.main(version_base=None, config_path="../config", config_name="01_submitit_hydra_example")
def main(config: DictConfig) -> None:
    """Example hydra + submitit pipeline"""
    logger.info("Starting job with the following config:")
    logger.info(OmegaConf.to_yaml(config, resolve=True))

    # Set up the output directory & logs directory
    out_dir = Path(config['out_dir'])
    logs_dir = Path(out_dir, "logs")
    Path(logs_dir).mkdir(parents=True, exist_ok=True)
    config_path = Path(out_dir, "config.yaml")
    logger.info(f"writing config to {config_path}")
    with open(config_path, "w") as f:
        OmegaConf.save(config, f, resolve=True)

    # Run the simple_function task via submitit
    executor = submitit.AutoExecutor(folder=Path(logs_dir))
    executor.update_parameters(
        name='simple_function',
        **config['submitit']
    )
    job = executor.submit(
        simple_function,
        **config['simple_function']
    )
    logger.info(f"Submitted job {job.job_id}")
    out_value = job.result()
    logger.info(f"Simple function returned {out_value}")
    
    logger.info("Done!")
    Path(out_dir, "done").touch()

if __name__ == "__main__":
    main()