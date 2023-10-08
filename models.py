from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)
    task_type = db.Column(db.String(20))  # 'todo', 'deadline', or 'event'
    due_time = db.Column(db.String(255), nullable=True)
    start_time = db.Column(db.String(255), nullable=True)
    end_time = db.Column(db.String(255), nullable=True)

    def __init__(self, title, task_type, due_time=None, start_time=None, end_time=None):
        self.title = title
        self.task_type = task_type
        self.due_time = due_time
        self.start_time = start_time
        self.end_time = end_time