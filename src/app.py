from flask import Flask
import flask
from flask import request
import json
from flask.json import jsonify

app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():

    json_text = flask.jsonify(todos)
    return json_text
todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[1]
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)