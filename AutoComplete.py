import re
from typing import List

import jellyfish

import Sentence
import numpy as np


def get_best_k_completions(user_input: str, dictionary: dict) -> List[Sentence.Sentence]:
    """
    :param user_input:
    :param dictionary:
    :return:
    """
    auto_completed_data = []
    query_prefix = [item.strip().lower()[0:3] for item in user_input.split()]
    intersection_of_set = intersection_of_sets(query_prefix, dictionary)
    for sentence in intersection_of_set:
        if user_input in sentence.__str__():
            offset = sentence.__str__().find(user_input)
            score = len(user_input) * 2
            sentence.set_score(score)
            sentence.set_offset(offset)
            auto_completed_data.append(sentence)
        if len(auto_completed_data) > 5:
            return auto_completed_data
    auto_completed_data.append(check_part_of_query(user_input, dictionary))
    return auto_completed_data


def intersection_of_sets(prefix_of_query: list[str], dictionary: dict) -> set[str]:
    set_of_prefix = [dictionary[key] for key in prefix_of_query if key in dictionary]
    if not set_of_prefix:
        return []
    sets_intersection = set.intersection(*set_of_prefix)
    return sets_intersection


def check_part_of_query(user_input: str, dictionary: dict) -> List[Sentence.Sentence]:
    results = []
    for word in user_input.split():
        new_list = [item.lower()[0:3] for item in user_input.split() if item not in [word]]
        set_intersection = intersection_of_sets(new_list, dictionary)
        for sentence in set_intersection:
            if check_validity(user_input, sentence) > 0:
                results.append(sentence)
    return results


def check_validity(user_input: str, sentence: str) -> int:
    first_word = user_input.split()[0]
    result = [_.start() for _ in re.finditer(first_word, user_input)]
    for place in result:
        sentence_substring = sentence.__str__()[place: place+len(user_input)]
        if jellyfish.damerau_levenshtein_distance(user_input, sentence_substring) <= 1:
            return calculate_points(user_input, sentence.__str__()[place: place+len(user_input)])
    return -1


def calculate_points(user_input, partial_sentence):
    return 15


def divide_user_input_to_3(user_input: str, word: str) -> tuple[str, str, str]:
    user_input_offset = user_input.find(word)
    sentence_begin = user_input[0, user_input_offset]
    sentence_middle = user_input[user_input_offset, user_input_offset + len(word)]
    sentence_end = user_input[user_input_offset + len(word), len(user_input)]
    return sentence_begin, sentence_middle, sentence_end


def levenshtein_distance(s, t):
    """ levenshtein_distance:
        Calculates levenshtein distance between two strings.
    """
    # Initialize matrix of zeros
    rows = len(s) + 1
    cols = len(t) + 1
    distance = np.zeros((rows, cols), dtype=int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0  # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                cost = 1
            distance[row][col] = min(distance[row - 1][col] + 1,  # Cost of deletions
                                     distance[row][col - 1] + 1,  # Cost of insertions
                                     distance[row - 1][col - 1] + cost)  # Cost of substitutions

    else:
        # This is the minimum number of edits needed to convert string a to string b
        return distance[row][col]
