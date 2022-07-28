import re
from typing import List

import jellyfish

import Sentence
import numpy as np


def get_best_k_completions(user_input: str, dictionary: dict) -> List[Sentence.Sentence]:
    """
    Run on the dictionary and find the top 5 results.

    :param user_input:
        The user sentence to search.
    :param dictionary:
        The dictionary of word prefix and sentences the prefix in.
    :return:
        Top 5 results.
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
    """
    Function to find the sets of the words and return the intersection between them.

    :param prefix_of_query:
        Prefix to find in the dictionary.
    :param dictionary:
        The dictionary to find in.
    :return:
        The intersection of the prefix sets.
    """
    set_of_prefix = [dictionary[key] for key in prefix_of_query if key in dictionary]
    if not set_of_prefix:
        return []
    sets_intersection = set.intersection(*set_of_prefix)
    return sets_intersection


def check_part_of_query(user_input: str, dictionary: dict) -> List[Sentence.Sentence]:
    """
    Function to get find the results base on part of the words in sentence.

    :param user_input:
        The sentence the user search.
    :param dictionary:
        The dictionary to search in.
    :return:
        List of the sentences with one mistake.
    """
    results = []
    for word in user_input.split():
        new_list = [item.lower()[0:3] for item in user_input.split() if item not in [word]]
        set_intersection = intersection_of_sets(new_list, dictionary)
        for sentence in set_intersection:
            if check_validity(user_input, sentence) > 0:
                results.append(sentence)
    return results


def check_validity(user_input: str, sentence: str) -> int:
    """
    Function to check the score of the user input compare to the sentence.

    :param user_input:
        The user sentence.
    :param sentence:
        The sentence from the dictionary to check.
    :return: -1 if
    the user input is not substring with 1 change, the sentence score if the user input is substring with 1 change.
    """
    first_word = user_input.split()[0]
    result = [_.start() for _ in re.finditer(first_word, user_input)]
    for place in result:
        sentence_substring = sentence.__str__()[place: place+len(user_input)]
        if jellyfish.damerau_levenshtein_distance(user_input, sentence_substring) <= 1:
            return calculate_points(user_input, sentence.__str__()[place: place+len(user_input)])
    return -1


def calculate_points(user_input, partial_sentence):
    return 15


def get_score(a, b):
    pos = dif(a, b)
    if a == b:
        return len(a) * 2
    elif len(a) == len(b):
        return len(a) * 2 - get_replace_score(pos)
    elif len(a) > len(b):
        return len(b) * 2 - get_deletion_addition_score(pos)
    elif len(a) < len(b):
        return len(a) * 2 - get_deletion_addition_score(pos)


def get_replace_score(position):
    if position[0] == 0:
        return 5
    elif position[0] == 1:
        return 4
    elif position[0] == 2:
        return 3
    elif position[0] == 3:
        return 2
    else:
        return 1


def get_deletion_addition_score(position):
    if position[0] == 0:
        return 10
    elif position[0] == 1:
        return 8
    elif position[0] == 2:
        return 6
    elif position[0] == 3:
        return 4
    else:
        return 2


def dif(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]
