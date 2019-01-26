class Config(object):
    DUMP_PATH = 'Database/Dumps/dump.pickle'
    SYNC = True
    FOLLOWER_URLS = [
        'http://127.0.0.1:5001/'
    ]
    TYPE = "master"
