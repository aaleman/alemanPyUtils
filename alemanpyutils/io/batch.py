

class Batch:
    __id_counter = 0

    def __init__(self, batch_size: int = 100, no_id: bool = False):
        self.__elems = []
        self.__id = 0
        self.__batch_size = batch_size
        self.__remote_error = False

        if not no_id:
            self.__generate_id()

    def is_full(self):
        return self.__batch_size <= len(self.__elems)

    def is_empty(self):
        return len(self.__elems) == 0

    def __generate_id(self):
        Batch.__id_counter = Batch.__id_counter + 1
        self.__id = Batch.__id_counter

    def add(self, elem):
        if not self.is_full():
            self.__elems.append(elem)
    
    def add_all(self, elems: []):

        if len(self.__elems) + len(elems) <= self.__batch_size:
            self.__elems.extend(elems)

    def get_elems(self):
        return self.__elems

    def get_batch_size(self):
        return self.__batch_size

    def set_id(self, new_id: int):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def is_last(self):
        return self.__id == -1

    @staticmethod
    def last():

        last = Batch(0)
        last.__id = -1
        return last