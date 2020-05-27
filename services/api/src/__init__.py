from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .routes import to_do, user


app = Flask(__name__)
app.config.from_object("src.config.Config")

db = SQLAlchemy(app)

app.register_blueprint(to_do.to_do_blueprint)
app.register_blueprint(user.user_blueprint)


db = SQLAlchemy(app)
