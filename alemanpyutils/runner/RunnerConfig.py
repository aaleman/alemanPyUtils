class RunnerConfig:
    def __init__(self, read_queue_size: int = 10,
                 write_queue_size: int=10,
                 num_processors: int = 1,
                 batch_size: int=1000, verbose: bool = True):
        super().__init__()
        self.read_queue_size = read_queue_size
        self.write_queue_size = write_queue_size
        self.num_processors = num_processors
        self.batch_size = batch_size
        self.verbose = verbose
