from queue import Queue
from threading import Thread

from alemanpyutils.runner.DataReader import DataReader
from alemanpyutils.runner.RunnerConfig import RunnerConfig
from alemanpyutils.runner.Batch import Batch


class Reader(Thread):

    def __init__(self, data_reader: DataReader, runner_config: RunnerConfig) -> None:
        super().__init__()
        self._data_reader = data_reader
        self._runner_config = runner_config

        self._batch_count = 0
        self.__read_queue = Queue(runner_config.read_queue_size)
        self.__batch_size = runner_config.batch_size
        self.__batch = self.__new_batch()
        self.__num_processors = runner_config.num_processors

    def run(self):
        self._data_reader.open()
        self._data_reader.pre()

        while self._data_reader.has_next():
            self.__add_elems_to_batch(self.__read())

        self.__finish_batch()

        self._data_reader.post()
        self._data_reader.close()

    def __read(self) -> []:
        return self._data_reader.read_batch(self.__batch_size)

    def __add_elems_to_batch(self, elems: []) -> None:
        for elem in elems:
            self.__add_elem_to_batch(elem)

    def __add_elem_to_batch(self, elem) -> None:

        self.__batch.add(elem)

        if self.__batch.is_full():
            self.__add_batch(self.__batch)
            self.__batch = self.__new_batch()

    def __new_batch(self) -> Batch:
        new_batch = Batch(self.__batch_size)
        return new_batch

    def __add_batch(self, batch) -> None:
        self.__read_queue.put(batch)
        self._batch_count += 1

    def __finish_batch(self) -> None:

        if not self.__batch.is_empty():
            self.__add_batch(self.__batch)

        for i in range(0, self.__num_processors):
            self.__read_queue.put(Batch.last())

    def take(self):
        return self.__read_queue.get()
