from alemanpyutils.io.Processor import Processor
from alemanpyutils.io.Reader import Reader
from alemanpyutils.io.RunnerConfig import RunnerConfig
from alemanpyutils.io.Writer import Writer


class Runner:
    def __init__(self, reader: Reader, writer: Writer, processors: [Processor], runner_config:RunnerConfig):
        super().__init__()
        self.__reader = reader
        self.__writer = writer
        self.__processors = processors
        self.__runner_config = runner_config

    def launch(self):

        self.__reader.name = "READER_THREAD"
        self.__writer.name = "WRITER_THREAD"

        self.__reader.start()
        for proc in self.__processors:
            proc.start()

        self.__writer.start()

        self.__reader.join()
        for proc in self.__processors:
            proc.join()
        self.__writer.join()



