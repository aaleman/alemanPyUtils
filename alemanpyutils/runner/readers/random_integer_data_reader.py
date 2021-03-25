from alemanpyutils.runner.readers.random_object_data_reader import RandomObjectDataReader
from alemanpyutils.random.random_integer_generator import RandomIntegerGenerator


class RandomIntegerDataReader(RandomObjectDataReader):

    def __init__(self,  num_values: int):
        super().__init__(RandomIntegerGenerator(), num_values)


