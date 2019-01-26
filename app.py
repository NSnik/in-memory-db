import requests
import pickle
from flask import request, abort
from multiprocessing import Process
from os import path
from App.Database.database import Database


class NodeApp:

    def __init__(self, config):
        self.database = Database(config.DUMP_PATH)
        self.sync = config.SYNC
        self.follower_urls = config.FOLLOWER_URLS

    def replicate(self, request_func, id_, data=None):
        for url in self.follower_urls:
            print("tyt")
            request_func(path.join(url, id_), data=data)

    def database_info(self):
        return 'Some DB info'

    def show_db_data(self):
        return str(self.database.data)

    def get_all_keys(self):
        return pickle.dumps(self.database.data.keys())

    def get(self, id_):
        res = self.database.get(id_)
        if res:
            return self.database.get(id_)
        else:
            abort(404)

    def put(self, id_):
        self.database.set(id_, request.data.decode())
        process = Process(target=self.replicate, args=(requests.put, id_, request.data.decode()))
        process.start()
        if self.sync:
            process.join()
        return 'done'

    def delete(self, id_):
        result = self.database.remove(id_)
        process = Process(target=self.replicate, args=(requests.delete, id_))
        process.start()
        if self.sync:
            process.join()
        if result:
            return 'done'
        else:
            abort(404)
