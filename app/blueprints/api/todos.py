from app.blueprints.auth.models import User
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
    todos = [p.to_dict() for p in Todo.query.all()]
    return jsonify(todos)

# # TEST ROUTE
# @api.route('/poster', methods=['POST'])
# def get_todo():
#     """
#     [GET] /api/poster
#     """
#     data = json.loads(request.data.decode('utf-8'))
#     u = User.query.filter_by(email=data['user_email']).first()
#     # print(u)
#     # todos = [p.to_dict() for p in Todo.query.all()]
#     return jsonify([p.to_dict() for p in  u.todos.all()])
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

# Create new post
@api.route('/todos', methods=['POST'])
def create_todo():
    """
    [POST] /api/todos
    """
    print(request.get_json())
    p = Post()
    p.from_dict(request.json)
    p.save()
    return jsonify({ 'message': 'CREATED POST' })

# Updating existing todos
@api.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
    """
    [PUT] /api/todos/<id>
    """
    post = Todo.query.get(id)
    post.from_dict(request.json)
    db.session.commit()
    return jsonify(post.to_dict())

# Delete existing todos
@api.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    """
    [DELETE] /api/todos/<id>
    """
    post = Todo.query.get(id)
    post.delete()
    return jsonify([p.to_dict() for p in Todo.query.all()])