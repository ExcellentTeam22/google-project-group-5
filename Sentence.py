class Sentence:
    def __init__(self, file_name, sentence):
        self.file_name = file_name
        self.sentence = sentence

    def get_file_name(self):
        return self.file_name

    def __str__(self):
        return self.sentence

    def __repr__(self):
        return self.sentence

    def __eq__(self, other):
        if isinstance(other, Sentence):
            return self.file_name == other.file_name and self.sentence == other.sentence
        else:
            return False

    def __hash__(self):
        return hash(self.sentence)