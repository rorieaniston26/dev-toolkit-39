import os
import shutil
from typing import List, Optional
from pathlib import Path

class FileSystemManager:
    """Utility class for routine cleanup operations."""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)

    def clear_directory(self, target_subdir: str, extensions: Optional[List[str]] = None) -> int:
        """Removes files matching extensions within a directory."""
        target = self.base_path / target_subdir
        if not target.exists():
            return 0

        count = 0
        for item in target.iterdir():
            if item.is_file():
                if extensions is None or item.suffix in extensions:
                    item.unlink()
                    count += 1
        return count

    def archive_logs(self, log_dir: str, archive_dir: str) -> None:
        """Moves log files to a dedicated archive directory."""
        src = self.base_path / log_dir
        dst = self.base_path / archive_dir
        
        if not src.exists():
            return

        dst.mkdir(parents=True, exist_ok=True)
        for log_file in src.glob('*.log'):
            shutil.move(str(log_file), str(dst / log_file.name))

def get_temp_path() -> Path:
    """Returns the system temporary directory path."""
    return Path(os.getenv('TEMP', '/tmp'))