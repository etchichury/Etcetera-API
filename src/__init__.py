from flask import Flask
from .to_do import to_do_blueprint

app = Flask(__name__)
app.register_blueprint(to_do_blueprint)
