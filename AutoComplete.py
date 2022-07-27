from typing import List

import Sentence


def get_best_k_completions(prefix: str, dictionary: dict) -> List[Sentence.Sentence]:
    """

    :param prefix:
    :param dictionary:
    :return:
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
            auto_completed_data.append(sentence)
    return auto_completed_data
