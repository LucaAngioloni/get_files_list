import os
import fnmatch
from typing import Generator


def _get_dir_content(path, include_folders, recursive):
    entries = os.listdir(path)
    for entry in entries:
        entry_with_path = os.path.join(path, entry)
        if os.path.isdir(entry_with_path):
            if include_folders:
                yield entry_with_path
            if recursive:
                for sub_entry in _get_dir_content(entry_with_path, include_folders, recursive):
                    yield sub_entry
        else:
            yield entry_with_path


def get_dir_content(path: str, include_folders: bool = False, recursive: bool = True, prepend_folder_name: bool = True, pattern: str = None, exclude_pattern: str = None) -> Generator[str, None, None]:
    """Function that recursively gets files that match a pattern in a given directory.

    Args:
        path (str): The directory where the files are.
        include_folders (bool, optional): Return not only files but folders as well. Defaults to False.
        recursive (bool, optional): If False, only files directly under the given path are returned; otherwise search in subfolders recursively. Defaults to True.
        prepend_folder_name (bool, optional): If false do not add the `path` to the returned file paths. Defaults to True.
        pattern (_type_, optional): A Unix Shell like pattern used to filter files (For exaple "*.jpg" would only return files ending in `.jpg`). Defaults to None.
        exclude_pattern (_type_, optional): A Unix Shell like pattern used to exclude files (For exaple "*.jpg" would exclude all files ending in `.jpg`). Defaults to None.

    Yields:
        str: A file path.
    """
    path_len = len(path) + (len(os.path.sep)
                            if not path.endswith(os.path.sep) else 0)
    for item in _get_dir_content(path, include_folders, recursive):
        if (pattern is None or fnmatch.fnmatch(item, pattern)) and (exclude_pattern is None or not fnmatch.fnmatch(item, exclude_pattern)):
            yield item if prepend_folder_name else item[path_len:]
