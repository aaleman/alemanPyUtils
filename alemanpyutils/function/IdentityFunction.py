from alemanpyutils.function.Function import Function


class IdentityFunction(Function):

    def __init__(self):
        super().__init__()

    def apply(self, elem):
        return elem

