import sys
import ExtractFileData


def get_user_input():
    """
    Get input from the user.
    :return: List of the query divide into words.
    """
    user_input = input("Enter search query")
    if user_input == '#':
        return user_input
    user_input = ExtractFileData.delete_punctuation_and_white_space(user_input)
    return user_input
    # query_words = [item.strip().lower() for item in input("Enter search query: ").split()]
    # return query_words


def find_least_frequent_word(words):
    """
    Find what is the least frequent word in the input provided in the dictionary.
    :param words: List of words to search.
    :return: The least frequent word from the dictionary that is also in the list.
    """
    max_int = sys.maxsize
    best = max_int
    least_frequent = words[0]
    for word in words:
        if len(word) >= 3:
            num_of_vals = len(dictionary.get(word[0:3]))
            if num_of_vals < best:
                best = num_of_vals
                least_frequent = word
    return least_frequent
