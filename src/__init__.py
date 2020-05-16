import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .to_do import to_do_blueprint

app = Flask(__name__)
app.register_blueprint(to_do_blueprint)

# Fix performance hits from a bad default config and silence the warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)
