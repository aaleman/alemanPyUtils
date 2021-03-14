from alemanpyutils.function.ToUpperCaseFunction import ToUpperCaseFunction
from alemanpyutils.io.Processor import Processor
from alemanpyutils.io.Reader import Reader
from alemanpyutils.io.Runner import Runner
from alemanpyutils.io.RunnerConfig import RunnerConfig
from alemanpyutils.io.Writer import Writer
from alemanpyutils.io.readers.RandomStringDataReader import RandomStringDataReader
from alemanpyutils.io.writers.StandardOutputWriter import StandardOutputWriter


def test_runner():

    rc = RunnerConfig(batch_size=10, num_processors=10)

    reader = Reader(data_reader=RandomStringDataReader(
        5, 100), runner_config=rc)

    writer = Writer(data_writer=StandardOutputWriter(), runner_config=rc)

    processors = []
    for i in range(0, rc.num_processors):
        processors.append(Processor(reader, ToUpperCaseFunction(), writer, rc))

    runner = Runner(reader, writer, processors, rc)
    runner.launch()
