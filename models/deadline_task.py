from app import db

class DeadlineTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    deadline = db.Column(db.String(50), nullable=False)

    task = db.relationship('Task', backref='deadline_task', uselist=False)
