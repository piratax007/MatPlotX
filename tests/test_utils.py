import os
import sys
from pathlib import Path

from utils.file_utils import file_path_exist
import pytest


def test_file_path_exist_true_for_existing_file(tmp_path: Path) -> None:
    p: Path = tmp_path / "file.txt"
    p.write_text("this file already exists")

    result = file_path_exist(p)

    assert result is True


def test_file_path_exist_returns_false_for_non_existing_path(
        tmp_path: Path
) -> None:
    p: Path = tmp_path / "this_file_does_not_exist.txt"

    result = file_path_exist(p)

    assert result is False


def test_file_path_exist_returns_true_for_existing_path_passed_as_string(
        tmp_path: Path
) -> None:
    p: Path = tmp_path / "this_file_exists.txt"
    p.write_text("this file exists")

    result = file_path_exist(str(p))

    assert result is True


def test_file_path_exist_returns_false_for_non_existing_path_passed_as_string(
        tmp_path: Path
) -> None:
    p: Path = tmp_path / "this_file_does_not_exist.txt"

    result = file_path_exist(str(p))

    assert result is False


@pytest.mark.skipif(sys.platform.startswith("win") and not os.getenv("CI"),
                    reason="Symlinks creation may require admin/dev mode on "
                           "Windows")
def test_file_path_exist_returns_false_for_symlink_to_existing_file(tmp_path: Path) -> None:
    real_file: Path = tmp_path / "file.txt"
    real_file.write_text("this file already exists")
    link_to_real_file: Path = tmp_path / "link_to_file.txt"

    try:
        link_to_real_file.symlink_to(real_file)
    except (OSError, NotImplementedError):
        pytest.skip("Symlinks are not supported on this platform/filesystem")

    result = file_path_exist(link_to_real_file)

    assert result is False


def test_file_path_exist_returns_false_for_directory(tmp_path: Path) -> None:
    d: Path = tmp_path / "a_directory"
    d.mkdir()

    result = file_path_exist(d)

    assert result is False