import os
import shutil
from pathlib import Path
from typing import Union, List

def cleanup_directory(path: Union[str, Path], extension: str = "*.tmp") -> int:
    """Removes files matching pattern in specified directory."""
    target_dir = Path(path)
    if not target_dir.is_dir():
        return 0

    count = 0
    for file_path in target_dir.glob(extension):
        try:
            file_path.unlink()
            count += 1
        except OSError:
            continue
    return count

def archive_logs(source: str, destination: str) -> bool:
    """Moves log files to archival directory structure."""
    src_path = Path(source)
    dest_path = Path(destination)

    if not src_path.exists():
        return False

    dest_path.mkdir(parents=True, exist_ok=True)
    
    try:
        for item in src_path.iterdir():
            if item.suffix == '.log':
                shutil.move(str(item), str(dest_path / item.name))
        return True
    except (shutil.Error, OSError):
        return False

def get_directory_size(path: str) -> int:
    """Calculates total bytes for files in directory."""
    root = Path(path)
    return sum(f.stat().st_size for f in root.rglob('*') if f.is_file())