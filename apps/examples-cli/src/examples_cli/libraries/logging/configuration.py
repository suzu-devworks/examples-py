import json
import re
from importlib.resources import as_file
from importlib.resources import files as resource_files
from logging import DEBUG, basicConfig
from logging.config import dictConfig
from pathlib import Path
from typing import Any

import yaml


def _find_logging_config() -> Path | None:
    for file in Path(".").glob("logging_config.*"):
        if re.match(r".+\.(json|yaml|yml)$", str(file), re.IGNORECASE):
            return file
    return None


def _default_yaml_config() -> Path:
    resource = resource_files(__package__)
    with as_file(resource.joinpath("logging_config.yaml")) as config:
        return config


def _make_directories(config: dict[str, Any]) -> None:
    for handler in config["handlers"]:
        if "filename" in config["handlers"][handler]:
            logfile = Path(config["handlers"][handler]["filename"])
            dir = Path(logfile).parent
            if not dir.exists():
                dir.mkdir()
    return


def configure_logging() -> None:
    config = _find_logging_config() or _default_yaml_config()
    suffix = config.suffix.lower()
    match suffix:
        case ".json":
            with open(config) as file:
                config_dict = json.load(file)
            _make_directories(config_dict)
            dictConfig(config_dict)

        case ".yaml" | ".yml":
            with open(config) as file:
                config_dict = yaml.safe_load(file)
            _make_directories(config_dict)
            dictConfig(config_dict)

        case _:
            basicConfig(
                level=DEBUG,
                format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            )
    return
