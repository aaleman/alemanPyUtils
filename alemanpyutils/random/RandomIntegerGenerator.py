from alemanpyutils.random.RandomGenerator import RandomGenerator
import random


class RandomIntegerGenerator(RandomGenerator):

    def __init__(self, max_value: int = 10000):
        self.__max_value = max_value

    def generate(self):
        n = random.randint(0, self.__max_value)
        return n
