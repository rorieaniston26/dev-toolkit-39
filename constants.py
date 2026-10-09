import os
from pathlib import Path
from typing import Final

# Project directory configuration
BASE_DIR: Final[Path] = Path(__file__).resolve().parent
LOG_DIR: Final[Path] = BASE_DIR / "logs"
DATA_DIR: Final[Path] = BASE_DIR / "data"

# Application settings
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3
ENV: Final[str] = os.getenv("APP_ENV", "development")

# Formatting and encoding
DEFAULT_ENCODING: Final[str] = "utf-8"
DATE_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"

# Resource limits
CHUNK_SIZE: Final[int] = 1024 * 1024  # 1MB
SUPPORTED_EXTENSIONS: Final[list[str]] = [".json", ".yaml", ".csv"]

def ensure_directories() -> None:
    """Initializes required filesystem paths."""
    LOG_DIR.mkdir(exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)

if __name__ == "__main__":
    ensure_directories()