from .import bp as api
from flask import jsonify, request
from app import db
from app.blueprints.todos.models import Todo

# All todos
@api.route('/todos', methods=['GET'])
def get_todos():
    """
    [GET] /api/todos
    """
    todos = [t.to_dict() for t in Todo.query.all()]
    return jsonify(todos)

# # TEST ROUTE
# @api.route('/todoer', methods=['POST'])
# def get_todo():
#     """
#     [GET] /api/todoer
#     """
#     data = json.loads(request.data.decode('utf-8'))
#     u = User.query.filter_by(email=data['user_email']).first()
#     # print(u)
#     # todos = [t.to_dict() for p in Todo.query.all()]
#     return jsonify([t.to_dict() for p in  u.todos.all()])
#     # return jsonify(todos)
# # TEST ROUTE

# Single todos
@api.route('/todos/<id>', methods=['GET'])
def get_todo(id):
    print(id)
    """
    [GET] /api/todos/<id>
    """
    return jsonify(Todo.query.get_or_404(id).to_dict()) 

# Create new todo
@api.route('/todos', methods=['POST'])
def create_todo():
    """
    [POST] /api/todos
    """
    print(request.get_json())
    t = Todo()
    t.from_dict(request.json)
    t.save()
    return jsonify({ 'message': 'CREATED POST' })

# Updating existing todos
@api.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
    """
    [PUT] /api/todos/<id>
    """
    todo = Todo.query.get(id)
    todo.from_dict(request.json)
    db.session.commit()
    return jsonify(todo.to_dict())

# Delete existing todos
@api.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    """
    [DELETE] /api/todos/<id>
    """
    todo = Todo.query.get(id)
    todo.delete()
    return jsonify([t.to_dict() for p in Todo.query.all()])