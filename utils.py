import logging
import re
import json
from pathlib import Path


def get_logger(name: str) -> logging.Logger:
    """
    Sets up and returns a logger with the specified name.
    Logs messages to the console with a specific format.
    """
    logging.basicConfig(
        level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
    )

    return logging.getLogger(name)
