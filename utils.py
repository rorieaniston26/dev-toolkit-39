import os
import shutil
import logging
from typing import List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('dev-toolkit-39')

def cleanup_temp_directories(paths: List[str]) -> int:
    """Removes list of temporary directory paths."""
    count = 0
    for path in paths:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                logger.info(f"Successfully removed: {path}")
                count += 1
            except OSError as e:
                logger.error(f"Failed to remove {path}: {e}")
    return count

def organize_project_files(target_dir: str, extensions: List[str]) -> None:
    """Moves files with specific extensions into a sub-folder."""
    if not os.path.exists(target_dir):
        return

    target_sub = os.path.join(target_dir, 'archived')
    os.makedirs(target_sub, exist_ok=True)

    for item in os.listdir(target_dir):
        if any(item.endswith(ext) for ext in extensions):
            src = os.path.join(target_dir, item)
            dst = os.path.join(target_sub, item)
            shutil.move(src, dst)
            logger.info(f"Moved {item} to {target_sub}")

if __name__ == '__main__':
    # Example utility execution
    organize_project_files('./data', ['.log', '.tmp'])
    cleanup_temp_directories(['./temp_cache'])