from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, type, description, done=False):
        self.type = type
        self.description = description
        self.done = done

    def as_dict(self):
        task_dict = {
            'id': self.id,
            'type': self.type,
            'description': self.description,
            'done': self.done
        }
        return task_dict

    def __repr__(self):
        return f"<Task(id={self.id}, type='{self.type}', description='{self.description}', done={self.done})>"
