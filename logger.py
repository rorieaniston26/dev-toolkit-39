import logging
import sys
from pathlib import Path
from typing import Any, Optional, Union


class ToolkitLogger:
    """Custom logger wrapper providing standardized output formatting for the toolkit."""

    def __init__(
        self,
        name: str = "dev_toolkit",
        level: Union[int, str] = logging.INFO,
        log_file: Optional[Union[str, Path]] = None,
    ) -> None:
        """Initialize logger instance with stdout and optional file handler.

        Args:
            name: Identifier for the logger instance.
            level: Log verbosity threshold (logging constant or string name).
            log_file: Optional path for persisting log output to file.
        """
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.handlers.clear()

        formatter: logging.Formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        if log_file:
            path: Path = Path(log_file)
            path.parent.mkdir(parents=True, exist_ok=True)
            file_handler: logging.FileHandler = logging.FileHandler(path)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def info(self, message: str, *args: Any) -> None:
        """Log an informational message."""
        self.logger.info(message, *args)

    def debug(self, message: str, *args: Any) -> None:
        """Log a detailed debug message."""
        self.logger.debug(message, *args)

    def warning(self, message: str, *args: Any) -> None:
        """Log a warning message indicating a potential issue."""
        self.logger.warning(message, *args)

    def error(self, message: str, exc_info: bool = False, *args: Any) -> None:
        """Log an error message with optional stack trace context."""
        self.logger.error(message, *args, exc_info=exc_info)


def get_default_logger() -> ToolkitLogger:
    """Factory function to construct a default toolkit logging instance."""
    return ToolkitLogger(name="dev_toolkit_default")
