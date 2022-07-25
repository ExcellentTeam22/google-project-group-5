from typing import IO, AnyStr


class FileData:
    file_name: str
    sentences: list[str]

    def __init__(self, name_of_file: str, file: IO[AnyStr]):
        """
        Initial the data in the file. save the data and the name of the file.
        :param name_of_file: The name of the file.
        :param file: The file to read from.
        """
        self.file_name = name_of_file
        self.sentences = file.readlines()

    def get_sentences(self) -> list[str]:
        """
        Getter function, return the sentences list.
        :return: The sentences list.
        """
        return self.sentences

    def get_name(self) -> str:
        """
        Getter function, return the file name.
        :return: The file name.
        """
        return self.file_name
