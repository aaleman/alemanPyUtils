from alemanpyutils.io.DataWriter import DataWriter


class StandardOutputWriter(DataWriter):

    def __init__(self) -> None:
        super().__init__()

    def write(self, elem) -> None:
        print(elem)
