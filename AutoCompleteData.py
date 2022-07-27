from dataclasses import dataclass

@dataclass
class AutoCompleteData:
    """An autocomplete object class which represents a single line of output

        Args:
        completed_sentence (str): The completed sentence.
        source_text (str): The name of the source file of the completed sentence

        Attributes:
            completed_sentence (str): The completed sentence.
            source_text (str): The name of the source file of the completed sentence
            offset (int): The offset of the user input in the completed_sentence
            score (int): The completed_sentence score, which is calculated like this:
                        -The base scoring is double the number of characters in the user input which have a match.
                        -Replacing character will decrease 5 point for first char, 2 points for second char, 3 point for third char,
                         2 point for fourth char and 1 point for fifth and more char.
                        - Deleting or addition of a character wil decrease 10 points for first character, 8 for second,
                          6 for third, 4 for fourth and 2 point for the rest.
    """

    completed_sentence: str
    source_text: str
    offset: int
    score: int

    # def __init__(self, source_text, completed_sentence):
    #     self.source_text = source_text
    #     self.completed_sentence = completed_sentence
    #
    # def get_source_text_name(self):
    #     return self.source_text
    #
    # def __str__(self):
    #     return self.completed_sentence
    #
    # def __repr__(self):
    #     return self.completed_sentence
    #
    # def __eq__(self, other):
    #     if isinstance(other, AutoCompleteData):
    #         return self.source_text == other.source_text and self.completed_sentence == other.completed_sentence
    #     else:
    #         return False
    #
    # def __hash__(self):
    #     return hash(self.completed_sentence)