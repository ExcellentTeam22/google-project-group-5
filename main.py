from typing import List
import AutoCompleteData
import zipfile
from FileData import FileData


def open_files(input_dir: str):
    """
    :param input_dir: str
    :return: none
    This functions receives a zip directory name.
    It opens it using the "zipfile" module, and then open each file in the
    files tree and sends it to a function which reads the file data.
    """
    with zipfile.ZipFile(input_dir, mode="r") as archive:
        input_files_paths = archive.namelist()
        for file_path in input_files_paths:
            with archive.open(file_path) as f:
                import os
                f_name, f_ext = os.path.splitext(file_path)
                FileData.FileData(f_name, f)


def get_best_k_completions(prefix: str) -> List[AutoCompleteData]:
    pass


if __name__ == "__main__":
    open_files("Archive.zip")
