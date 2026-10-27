import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    standardized logger configuration for dev-toolkit-39 modules
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_data_structure(logger: logging.Logger, data: dict, label: str = "data") -> None:
    """
    formatted logging for dict structures
    """
    import json
    try:
        formatted = json.dumps(data, indent=4, sort_keys=True)
        logger.info(f"dumping {label}:\n{formatted}")
    except (TypeError, ValueError) as e:
        logger.error(f"failed to serialize {label}: {e}")