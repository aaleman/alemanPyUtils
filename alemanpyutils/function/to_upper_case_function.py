import string

from alemanpyutils.function.function import Function


class ToUpperCaseFunction(Function):

    def __init__(self):
        super().__init__()

    def apply(self, elem:  string) -> string:
        return elem.upper()
