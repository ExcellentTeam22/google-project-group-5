import string
from typing import IO, AnyStr
import re
import Sentence


def update_dictionary(name_of_line: str, line: str, word_prefix_dictionary :dict):
    """

    :param word_prefix_dictionary:
    :param name_of_line:
    :param line:
    :return:
    """
    line = delete_punctuation_and_white_space(line)
    line = line.lower()
    line_words = line.split()
    sentence = Sentence.Sentence(name_of_line, line)
    for word in line_words:
        new_word = word
        if len(word) >= 3:
            new_word = word[0:3]
        else:
            continue
        if new_word in word_prefix_dictionary:
            word_prefix_dictionary[new_word].add(sentence)
            # print(word_prefix_dictionary)
        else:
            word_prefix_dictionary[new_word] = {sentence}
            # print(word_prefix_dictionary)


def delete_punctuation_and_white_space(line: str) -> str:
    new_string = str(line).translate(str.maketrans('', '', string.punctuation))
    new_string = re.sub(' +', ' ', new_string)
    return new_string.strip()


class ExtractFileData:
    def __init__(self, file_name: str, file: IO[AnyStr], word_prefix_dictionary: dict):
        self.file_name = file_name.split("/")[-1]
        self.file = file
        while True:
            line = file.readline()
            if not line:
                break
            update_dictionary(self.file_name, line, word_prefix_dictionary)
