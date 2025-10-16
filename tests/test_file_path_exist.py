from pathlib import Path

from utils.file_utils import file_path_exist


def test_file_path_exist_true_for_existing_file(tmp_path: Path) -> None:
    p: Path = tmp_path / "file.txt"

    result = file_path_exist(p)

    assert result is True