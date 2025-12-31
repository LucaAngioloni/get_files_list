from __future__ import annotations

import fnmatch
import os
from typing import Generator, Sequence


def _get_dir_content(
    path: str, include_folders: bool, recursive: bool
) -> Generator[str, None, None]:
    entries: list[str] = os.listdir(path)
    for entry in entries:
        entry_with_path = os.path.join(path, entry)
        if os.path.isdir(entry_with_path):
            if include_folders:
                yield entry_with_path
            if recursive:
                for sub_entry in _get_dir_content(
                    entry_with_path, include_folders, recursive
                ):
                    yield sub_entry
        else:
            yield entry_with_path


def get_dir_content(
    path: str,
    include_folders: bool = False,
    recursive: bool = True,
    prepend_folder_name: bool = True,
    pattern: str | Sequence[str] | None = None,
    exclude_pattern: str | Sequence[str] | None = None,
) -> Generator[str, None, None]:
    """Function that recursively gets files that match a pattern in a given directory.

    Args:
        path (str): The directory where the files are.
        include_folders (bool, optional): Return not only files but folders as well. Defaults to False.
        recursive (bool, optional): If False, only files directly under the given path are returned; otherwise search in subfolders recursively. Defaults to True.
        prepend_folder_name (bool, optional): If false do not add the `path` to the returned file paths. Defaults to True.
        pattern (str | list, optional): A Unix Shell like pattern used to filter files (For exaple "*.jpg" would only return files ending in `.jpg`). Defaults to None. You can also pass a list of patterns to match and if any the path will be returned.
        exclude_pattern (str | list, optional): A Unix Shell like pattern used to exclude files (For exaple "*.jpg" would exclude all files ending in `.jpg`). Defaults to None. You can also pass a list of patterns to exclude and if any the path will be excluded.

    Yields:
        str: A file path.
    """
    path_len = len(path) + (len(os.path.sep) if not path.endswith(os.path.sep) else 0)

    if pattern is None:
        patterns: Sequence[str] | None = None
    elif isinstance(pattern, str):
        patterns = [pattern]
    else:
        patterns = pattern

    if exclude_pattern is None:
        exclude_patterns: Sequence[str] | None = None
    elif isinstance(exclude_pattern, str):
        exclude_patterns = [exclude_pattern]
    else:
        exclude_patterns = exclude_pattern

    for item in _get_dir_content(path, include_folders, recursive):
        if (patterns is None or any(fnmatch.fnmatch(item, p) for p in patterns)) and (
            exclude_patterns is None
            or not any(fnmatch.fnmatch(item, ep) for ep in exclude_patterns)
        ):
            yield item if prepend_folder_name else item[path_len:]
