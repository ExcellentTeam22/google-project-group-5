import sys
import ExtractFileData


def get_user_input() -> str:
    """
    Receives input from the user and sends it to a function that removes all white spaces and punctuation marks.
    :return: String of the user input without white spaces and punctuation marks.
    """
    user_input = input("[+] Enter search query\n")
    if user_input == '#':
        return user_input
    user_input = ExtractFileData.delete_punctuation_and_white_space(user_input)
    return user_input
