from dataclasses import dataclass

@dataclass
class AutoCompleteData:
    """An autocomplete object class which represents a single line of output

        Args:


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
    # methods that you need to define by yourself