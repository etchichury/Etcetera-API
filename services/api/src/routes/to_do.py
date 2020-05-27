from flask import Blueprint


to_do_blueprint = Blueprint('todo_blueprint', 'to_do', url_prefix="/todo")


@to_do_blueprint.route("/")
def index():
    return "This is the TODO route"
