from threading import Thread

from alemanpyutils.function.Function import Function
from alemanpyutils.io.Reader import Reader
from alemanpyutils.io.RunnerConfig import RunnerConfig
from alemanpyutils.io.Writer import Writer
from alemanpyutils.io.batch import Batch


class Processor(Thread):
    def __init__(self, reader: Reader, function: Function, writer: Writer, runner_config: RunnerConfig):
        super().__init__()

        self._reader = reader
        self._function = function
        self._writer = writer
        self._runner_config = runner_config

    def run(self):
        while True:
            batch = self._get_from_read_queue()

            if batch.is_last():
                break

            res = self._apply(batch)
            self._add_to_write_queue(res)

        self._add_last_to_write_queue()

    def _get_from_read_queue(self) -> Batch:
        return self._reader.take()

    def _add_to_write_queue(self, res: Batch):
        self._writer.put(res)

    def _add_last_to_write_queue(self):
        self._writer.put_last()

    def _apply(self, batch: Batch) -> Batch:
        new_batch = Batch(batch.get_batch_size(), True)
        new_batch.set_id(batch.get_id())

        for elem in batch.get_elems():
            new_batch.add(self._function.apply(elem))

        return new_batch





