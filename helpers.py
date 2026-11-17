import os
import shutil
from pathlib import Path
from typing import List, Optional

def clear_directory(target_path: str, extensions: Optional[List[str]] = None) -> None:
    """Removes files from directory based on optional extension filter."""
    target = Path(target_path)
    if not target.is_dir():
        return

    for item in target.iterdir():
        if item.is_file():
            if extensions is None or item.suffix in extensions:
                item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

def organize_files(source_dir: str, target_map: dict) -> None:
    """Moves files into subdirectories based on extension mapping."""
    source = Path(source_dir)
    if not source.exists():
        return

    for file_path in source.iterdir():
        if file_path.is_file():
            category = target_map.get(file_path.suffix, 'others')
            dest_dir = source / category
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(dest_dir / file_path.name))

def get_directory_size(path: str) -> int:
    """Calculates total bytes for files in directory."""
    total = 0
    for root, _, files in os.walk(path):
        for file in files:
            total += os.path.getsize(os.path.join(root, file))
    return total