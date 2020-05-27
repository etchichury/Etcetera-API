from flask import Blueprint


user_blueprint = Blueprint("user_blueprint", "user", url_prefix="/user")


@user_blueprint.route("/")
def index():
    return "This is the User route"
