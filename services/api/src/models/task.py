import pytz
from datetime import datetime

from .. import db


class Task(db.Model):
    __tablename__ = "Tasks"

    timezone = pytz.timezone("Etc/GMT3")
    datetime_now = datetime.now(timezone)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    created_at = db.Column(db.DataTime, nullable=False, default=datetime_now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Task {self.title}"
