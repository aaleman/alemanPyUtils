from queue import Queue
from threading import Thread

from alemanpyutils.runner.DataWriter import DataWriter
from alemanpyutils.runner.RunnerConfig import RunnerConfig
from alemanpyutils.runner.Batch import Batch


class Writer(Thread):

    def __init__(self, data_writer: DataWriter, runner_config: RunnerConfig):
        super().__init__()
        self._data_writer = data_writer
        self.__write_queue = Queue(runner_config.write_queue_size)
        self.__num_processors = runner_config.num_processors
        self.__finished_processors = 0

    def run(self):
        self._data_writer.open()
        self._data_writer.pre()

        while not self.__is_finished():
            batch = self.__get_batch()

            if batch.is_last():
                continue

            self._data_writer.write_batch(batch)

        self._data_writer.post()
        self._data_writer.close()

    def __get_batch(self) -> Batch:
        batch = self.__write_queue.get()

        if batch.is_last():
            self.__finished_processors += 1

        return batch

    def __is_finished(self) -> bool:
        return self.__finished_processors >= self.__num_processors

    def put(self, batch: Batch):
        self.__write_queue.put(batch)

    def put_last(self) -> None:
        self.put(Batch.last())
