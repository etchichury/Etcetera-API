from .. import db


class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    tasks = db.relationship("Tasks", backref="user", lazy=True)

    def __repr__(self):
        return f"User {self.name}"
