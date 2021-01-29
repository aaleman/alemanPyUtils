import random
import string

from alemanpyutils.random.RandomGenerator import RandomGenerator


class RandomStringGenerator(RandomGenerator):

    def __init__(self, length: int = 10000):
        self.__length = length

    def generate(self):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(self.__length))

        return result_str
