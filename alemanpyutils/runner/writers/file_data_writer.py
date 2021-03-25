from alemanpyutils.runner.writers.data_writer import DataWriter


class FileDataWriter(DataWriter):

    def __init__(self, file_name) -> None:
        super().__init__()
        self.__file_name = file_name
        self.__file_handler = None

    def open(self) -> None:
        self.__file_handler = open(self.__file_name, "w")

    def write(self, elem):
        self.__file_handler.write(str(elem) + "\n")

    def close(self) -> None:
        self.__file_handler.close()





