from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.title

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'is_completed': self.is_completed,
        }


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
        }