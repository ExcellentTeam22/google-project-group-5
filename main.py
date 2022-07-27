import ExtractFileData
import zipfile
import os
import math
import AutoComplete

import UserInput
from Sentence import Sentence

files = []
word_prefix_dictionary = {}


def open_files(input_dir: str):
    """
    This functions receives a zip directory name.
    It opens it using the "zipfile" module, and then open each file in the
    files tree and sends it to a function which reads the file data.

    :param:
        input_dir: The path to a directory
    :return:
        none
    """
    with zipfile.ZipFile(input_dir, mode="r") as archive:
        input_files_paths = archive.namelist()
        for file_path in input_files_paths:
            with archive.open(file_path) as f:
                f_name, f_ext = os.path.splitext(file_path)
                ExtractFileData.ExtractFileData(f_name, f, word_prefix_dictionary)
    # with open("test.txt.txt") as f:
    #     ExtractFileData.ExtractFileData("sds", f, word_prefix_dictionary)


def count_prefix_appearances() -> set[str]:
    """
    This functions counts each key appearances in the prefix dictionary
    by checking the size of each of its values(when each value is a set of sentences).
    If the prefix appear more the log(n) times, then it will be added to a set of most common prefix.

    :return:
        set of most common prefix.

    """

    most_common_prefix = set()
    dictionary_values_counter = 0
    for value in word_prefix_dictionary.values():
        dictionary_values_counter += len(value)

    upper_limit = math.log10(dictionary_values_counter)
    for key, value in word_prefix_dictionary:
        if len(value) >= upper_limit:
            most_common_prefix.add(key)

    return most_common_prefix


if __name__ == "__main__":
    # with open("test.txt.txt") as f:
    #     read_file("test.txt.txt", f)
    # get_best_k_completions("would")
    # print(dictionary)
    # open_files("Archive.zip")
    # for file in files:
    #     print(file.get_name())
    print("[+] Loading files and preparing the system...")
    open_files("Archive.zip")
    print("[+] The system is ready.")

    while True:
        the_user_input = UserInput.get_user_input()
        print(AutoComplete.get_best_k_completions(the_user_input, word_prefix_dictionary))
        print(the_user_input)
        next_input = UserInput.get_user_input()
        while next_input != '#':
            the_user_input = the_user_input + " " + next_input
            print(AutoComplete.get_best_k_completions(the_user_input, word_prefix_dictionary))
            print(the_user_input)
            next_input = UserInput.get_user_input()
        the_user_input = ""
