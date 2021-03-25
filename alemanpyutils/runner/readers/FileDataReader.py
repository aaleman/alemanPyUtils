from alemanpyutils.runner.DataReader import DataReader


class FileDataReader(DataReader):

    def __init__(self, file_name) -> None:
        super().__init__()
        self.__file_name = file_name
        self.__file_handler = None
        self.__line = None

    def open(self) -> None:
        self.__file_handler = open(self.__file_name, "r")

    def pre(self) -> None:
        self.__next_line()

    def has_next(self):
        return self.__line is not None

    def next(self):
        res  = self.__line
        self.__next_line()
        return res

    def __next_line(self):
        self.__line = self.__file_handler.readline()

    def close(self) -> None:
        self.__file_handler.close()





