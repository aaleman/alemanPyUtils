from alemanpyutils.function.to_upper_case_function import ToUpperCaseFunction
from alemanpyutils.runner.processors.processor import Processor
from alemanpyutils.runner.readers.reader import Reader
from alemanpyutils.runner.runner import Runner
from alemanpyutils.runner.runner_config import RunnerConfig
from alemanpyutils.runner.writers.writer import Writer
from alemanpyutils.runner.readers.random_string_data_reader import RandomStringDataReader
from alemanpyutils.runner.writers.standard_output_writer import StandardOutputWriter


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
