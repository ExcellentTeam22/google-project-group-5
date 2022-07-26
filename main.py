import ExtractFileData
import zipfile
import os

files = []
word_prefix_dictionary = {}


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
                f_name, f_ext = os.path.splitext(file_path)
                ExtractFileData.ExtractFileData(f_name, f, word_prefix_dictionary)
    # with open("test.txt.txt") as f:
    #     ExtractFileData.ExtractFileData("sds", f, word_prefix_dictionary)


def get_best_k_completions(prefix: str):  # -> List[AutoCompleteData]:
    words = prefix.split()
    sentences = []
    for word in words:
        if len(word) >= 3:
            sentences = get_sentences(word[0:3])
        else:
            sentences = get_sentences(word)
    for sentence in sentences:
        if prefix in sentence:
            print(sentence)


def get_sentences(sub_string):
    return word_prefix_dictionary[sub_string]


if __name__ == "__main__":
    # with open("test.txt.txt") as f:
    #     read_file("test.txt.txt", f)
    # get_best_k_completions("would")
    # print(dictionary)
    # open_files("Archive.zip")
    # for file in files:
    #     print(file.get_name())
    open_files("Archive.zip")

    print(word_prefix_dictionary)
