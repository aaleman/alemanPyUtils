from alemanpyutils.runner.batch import Batch


class DataWriter:

    def open(self) -> None:
        pass

    def close(self) -> None:
        pass

    def pre(self) -> None:
        pass

    def post(self) -> None:
        pass

    def write_batch(self, batch: Batch) -> None:
        for elem in batch.get_elems():
            self.write(elem)

    def write(self, elem) -> None:
        pass
