from os import path
import pickle


class Database:

    def __init__(self, dump_path):
        self.data = {}
        self.dump_path = dump_path

        if path.isfile(self.dump_path):
            with open(self.dump_path, 'rb') as handle:
                self.data = pickle.load(handle)

    def get(self, id_):
        return self.data.get(id_)

    def set(self, id_, value):
        self.data[id_] = value
        self.dump()

    def remove(self, id_):
        try:
            self.data.pop(id_)
            self.dump()
            return True
        except KeyError:
            return False

    def dump(self):
        with open(self.dump_path, 'wb+') as handle:
            pickle.dump(self.data, handle, protocol=pickle.HIGHEST_PROTOCOL)
