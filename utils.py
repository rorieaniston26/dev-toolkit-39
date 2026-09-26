import os
import shutil
from pathlib import Path
from typing import List, Optional

def cleanup_directory(directory: str, extensions: Optional[List[str]] = None) -> int:
    """Removes files with specific extensions from the target directory."""
    count = 0
    path = Path(directory)
    
    if not path.is_dir():
        return count

    for item in path.iterdir():
        if item.is_file():
            if extensions is None or item.suffix in extensions:
                item.unlink()
                count += 1
    return count

def reorganize_files(source: str, destination: str, pattern: str = "*") -> None:
    """Moves files matching a pattern from source to destination."""
    src_path = Path(source)
    dst_path = Path(destination)
    
    dst_path.mkdir(parents=True, exist_ok=True)
    
    for file in src_path.glob(pattern):
        if file.is_file():
            shutil.move(str(file), str(dst_path / file.name))

def get_directory_size(path: str) -> int:
    """Calculates total size of files in a directory."""
    return sum(f.stat().st_size for f in Path(path).rglob('*') if f.is_file())

if __name__ == "__main__":
    # Example usage for dev-toolkit-39 routine maintenance
    print(f"Cleanup started for path: {os.getcwd()}")