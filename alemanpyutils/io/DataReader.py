class DataReader:

    def open(self) -> None:
        pass

    def close(self) -> None:
        pass

    def pre(self) -> None:
        pass

    def post(self) -> None:
        pass

    def read_batch(self, batch_size) -> []:
        res = []

        i = 0

        while self.has_next() and i <= batch_size:
            elem = self.next()
            res.append(elem)
            i += 1

        return res

    def next(self):
        return self.read()

    def has_next(self):
        return False

    def read(self):
        pass
