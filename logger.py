import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "app",
    log_file: Optional[str] = "app.log",
    level: int = logging.INFO,
    max_bytes: int = 10_000_000,
    backup_count: int = 5,
    log_to_console: bool = True
) -> logging.Logger:
    """Configures and returns a logger instance with file rotation."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if already configured
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if log_file:
        # Ensure destination directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
