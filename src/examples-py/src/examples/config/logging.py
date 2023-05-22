import json
import logging
import re
from importlib.resources import as_file
from importlib.resources import files as resource_files
from logging import DEBUG, Filter, basicConfig
from logging.config import dictConfig
from pathlib import Path
from typing import Any

import yaml


class NoPasswordFilter(Filter):
    def __init__(self, name: str = "") -> None:
        super().__init__(name)

    def filter(self, record):
        log_message = record.getMessage()
        return "password" not in log_message


def level_and_below_filter_factory(level: str):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter


def __find_logging_config() -> Path:
    for file in Path(".").glob("logging_config.*"):
        if re.match(r".+\.(json|yaml|yml)$", str(file), re.IGNORECASE):
            return file
    return None


def __default_yaml_config() -> Path:
    resource = resource_files("examples.resources")
    with as_file(resource.joinpath("logging_config.yaml")) as config:
        return config


def __make_directories(config: dict[str, Any]):
    for handler in config["handlers"]:
        if "filename" in config["handlers"][handler]:
            logfile = Path(config["handlers"][handler]["filename"])
            dir = Path(logfile).parent
            if not dir.exists():
                dir.mkdir()
    return


def configure_logging():
    config = __find_logging_config() or __default_yaml_config()
    suffix = config.suffix.lower()
    match suffix:
        case ".json":
            with open(config) as file:
                config_dict = json.load(file)
            __make_directories(config_dict)
            dictConfig(config_dict)

        case ".yaml" | ".yml":
            with open(config) as file:
                config_dict = yaml.safe_load(file)
            __make_directories(config_dict)
            dictConfig(config_dict)

        case _:
            basicConfig(
                level=DEBUG,
                format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            )
    return
