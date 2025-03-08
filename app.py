from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():():
    todo = request.jsonest.json

    # add item only if it is not already present it is not already present
    if todo in todos:
        return jsonify({'error': 'Item already exists'}), 400 return jsonify({'error': 'Item already exists'}), 400
    else:
        todos.append(todo)do)
        return jsonify(todo), 201        return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])nt:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id >= len(todos) or todo_id < 0:do_id >= len(todos) or todo_id < 0:
        return jsonify({'error': 'Todo not found'}), 404rror': 'Todo not found'}), 404
    todo = request.json
    todos[todo_id] = todoodo_id] = todo
    return jsonify(todo), 200    return jsonify(todo), 200

@app.route('/todos/<int:todo_id>', methods=['DELETE'])odo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id >= len(todos) or todo_id < 0:
        return jsonify({'error': 'Todo not found'}), 404{'error': 'Todo not found'}), 404
    todo = todos.pop(todo_id)_id)
    return jsonify(todo), 200

if __name__ == '__main__':
    app.run(debug=True)