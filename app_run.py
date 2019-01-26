from flask import Flask
from app import NodeApp
from App.Config.config_1 import Config

app = Flask(__name__)
node = NodeApp(Config)

@app.route('/')
def index_route():
    return node.database_info()


@app.route('/<id_>', methods=['GET'])
def get_route(id_):
    return node.get(id_)


@app.route('/show', methods=['GET'])
def get_all_route():
    return node.show_db_data()


@app.route('/keys', methods=['GET'])
def get_all():
    return node.get_all_keys()


@app.route('/<id_>', methods=['PUT'])
def put_route(id_):
    return node.put(id_)


@app.route('/<id_>', methods=['DELETE'])
def delete_route(id_):
    return node.delete(id_)


if __name__ == '__main__':
    app.run()
