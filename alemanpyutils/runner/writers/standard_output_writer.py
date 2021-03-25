from alemanpyutils.runner.writers.data_writer import DataWriter


class StandardOutputWriter(DataWriter):

    def __init__(self) -> None:
        super().__init__()

    def write(self, elem) -> None:
        print(elem)
