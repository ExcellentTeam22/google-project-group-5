import string
from typing import IO, AnyStr
import re
import Sentence


class ExtractFileData:
    """An ExtractFileData object class is an functional class which devices a text file
        and splits it into a dictionary which its keys are the prefixes of the words in the text file
        and the values are sets of a Sentences objects.

               Args:
              source_text (str): The name of the source file of the sentence.
              file (IO[AnyStr]): A text file
              word_prefix_dictionary (dict) : dictionary which its keys are the prefixes of the words in the text file
                                              and the values are sets of a Sentences objects.
               Attributes:
                    source_text (str): The name of the source file of the sentence.
                    file (IO[AnyStr]): A text file
           """


    def __init__(self, source_text: str, file: IO[AnyStr], word_prefix_dictionary: dict):
        self.source_text = source_text.split("/")[-1]
        self.file = file
        while True:
            line = file.readline()
            if not line:
                break
            update_dictionary(self.source_text, line, word_prefix_dictionary)


def update_dictionary(source_text: str, line: str, word_prefix_dictionary :dict):
    """
    Checking if prefix of each word in a given sentence is already a key in the dictionary,
    if it does - Creating a Sentence object and adding it to the value.
    If it doesn't - adding it as a new key and the Sentence object to the value.
    :param
        word_prefix_dictionary(dict): dictionary which its keys are the prefixes of the words in the text file
                                and the values are sets of a Sentences objects.
    :param
        source_text(str): The name of the source file of the completed sentence
    :param
        line(str): Complete sentence
    :return:
        none
    """
    line = delete_punctuation_and_white_space(line)
    line = line.lower()
    line_words = line.split()
    sentence = Sentence.Sentence(source_text, line)
    for word in line_words:
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
    """
    Removes all white spaces and punctuation marks from a given string.

    :param
        line: Text string
    :return:
        Text string without spaces and punctuation marks.
    """
    new_string = str(line).translate(str.maketrans('', '', string.punctuation))
    new_string = re.sub(' +', ' ', new_string)
    return new_string.strip()


