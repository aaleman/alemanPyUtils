from alemanpyutils.runner.readers.RandomObjectDataReader import RandomObjectDataReader
from alemanpyutils.random.RandomIntegerGenerator import RandomIntegerGenerator


class RandomIntegerDataReader(RandomObjectDataReader):

    def __init__(self,  num_values: int):
        super().__init__(RandomIntegerGenerator(), num_values)


