from pathlib import Path
from typing import Union


def file_path_exist(path: Union[str, Path]) -> bool:
    p = Path(path)
    try:
        if p.is_symlink() or p.is_dir():
            return False
        return p.is_file()
    except OSError:
        return False