from alemanpyutils.runner.readers.random_object_data_reader import RandomObjectDataReader
from alemanpyutils.random.random_string_generator import RandomStringGenerator


class RandomStringDataReader(RandomObjectDataReader):

    def __init__(self,  length: int, num_values: int):
        super().__init__(RandomStringGenerator(length), num_values)


