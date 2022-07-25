from typing import List, IO, AnyStr
import AutoCompleteData
import zipfile
import FileData

files = []


def open_files(input_dir: str):
    """
    :param input_dir: The path to a directory
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
                #files.append(FileData.FileData(f_name, f))


# def get_best_k_completions(prefix: str) -> List[AutoCompleteData]:
#     pass

dictionary = {}


def read_file(name_of_file: str, file: IO[AnyStr]):
    """
    Read file
    :param name_of_file: name of txt file
    :param file: open txt file
    :return: none
    """
    while True:
        line = file.readline()
        if not line:
            break
        update_dictionary(name_of_file, line.split(), line)


def update_dictionary(name_of_line: str, words: list[str], line: str):
    """

    :param name_of_line:
    :param words:
    :param line:
    :return:
    """
    for word in words:
        new_word = word
        if len(word) > 3:
            new_word = word[0:3]
        if new_word in dictionary:
            dictionary[new_word].append(line)
        else:
            dictionary[new_word] = [line]


if __name__ == "__main__":
    with open("test.txt.txt") as f:
        read_file("test.txt.txt",f)
    print(dictionary)
    # open_files("Archive.zip")
    # for file in files:
    #     print(file.get_name())
