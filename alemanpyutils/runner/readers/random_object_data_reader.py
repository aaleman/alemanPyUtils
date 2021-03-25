from alemanpyutils.runner.readers.data_reader import DataReader
from alemanpyutils.random.random_generator import RandomGenerator


class RandomObjectDataReader(DataReader):

    def __init__(self, random_generator: RandomGenerator, num_values: int):
        self._count = 0
        self._num_values = num_values
        self._random_generator = random_generator

    def has_next(self):
        return self._count < self._num_values

    def next(self):
        next_obj = self._random_generator.generate()
        self._count += 1
        return next_obj
