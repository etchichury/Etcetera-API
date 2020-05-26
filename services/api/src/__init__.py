from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .to_do import to_do_blueprint

app = Flask(__name__)
app.config.from_object("src.config.Config")
app.register_blueprint(to_do_blueprint)


db = SQLAlchemy(app)
