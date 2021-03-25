from alemanpyutils.runner.readers.RandomObjectDataReader import RandomObjectDataReader
from alemanpyutils.random.RandomStringGenerator import RandomStringGenerator


class RandomStringDataReader(RandomObjectDataReader):

    def __init__(self,  length: int, num_values: int):
        super().__init__(RandomStringGenerator(length), num_values)


