class Sentence:
    """
    A sentence object class which represents a single line of text for a text file

        Args:
            sentence (str): The complete sentence.
            source_text (str): The name of the source file of the sentence

        Attributes:
            sentence (str): The complete sentence.
            source_text (str): The name of the source file of the sentence
    """
    completed_sentence: str
    source_text: str
    offset: int
    score: int

    def __init__(self, source_text, sentence):
        self.source_text = source_text
        self.sentence = sentence

    def set_score(self, score):
        self.score = score

    def set_offset(self, offset):
        self.offset = offset

    def get_file_name(self):
        return self.source_text

    def __str__(self):
        return self.sentence

    def __repr__(self):
        return self.sentence

    def __eq__(self, other):
        if isinstance(other, Sentence):
            return self.source_text == other.source_text and self.sentence == other.sentence
        else:
            return False

    def __hash__(self):
        return hash(self.sentence)