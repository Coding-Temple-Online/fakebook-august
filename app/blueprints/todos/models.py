from app import db
from datetime import datetime as dt

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    complete = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'complete': self.complete,
        }
        return data

    def from_dict(self, data):
        for field in ['title']:
            if field in data:
                setattr(self, field, data[field])