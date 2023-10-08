from app import db

class EventTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    start_time = db.Column(db.String(50), nullable=False)
    end_time = db.Column(db.String(50), nullable=False)

    task = db.relationship('Task', backref='event_task', uselist=False)
