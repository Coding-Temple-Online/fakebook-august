from flask import Blueprint

bp = Blueprint('todos', __name__, url_prefix='/todos')

from .import models