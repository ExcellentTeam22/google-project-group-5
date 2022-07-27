from typing import List

import Sentence
import numpy as np


def get_best_k_completions(prefix: str, dictionary: dict) -> List[Sentence.Sentence]:
    """
    Get 5 top suggestions of completed sentences from the query that was provided.
    :param prefix: The search query.
    :param dictionary: The prefix dictionary.
    :return: List of the top 5 suggestions of sentences.
    """
    auto_completed_data = [Sentence.Sentence]
    query_prefix = [item.strip().lower()[0:3] for item in prefix.split()]
    set_of_prefix = [dictionary[key] for key in query_prefix if key in dictionary]
    intersection_of_sets: set[Sentence.Sentence] = set.intersection(*set_of_prefix)
    for sentence in intersection_of_sets:
        if prefix in sentence.__str__():
            offset = sentence.__str__().find(prefix)
            score = len(prefix) * 2
            sentence.set_score(score)
            sentence.set_offset(offset)
            if len(auto_completed_data) == 5:
                break
            auto_completed_data.append(sentence)
    return auto_completed_data


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
