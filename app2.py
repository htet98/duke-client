from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///duke.db'  # Replace with your database URL
db = SQLAlchemy(app)

# Define models for your database tables
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)

class DeadlineTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    deadline = db.Column(db.String(50), nullable=False)

    task = db.relationship('Task', backref='deadline_task', uselist=False)

class EventTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    start_time = db.Column(db.String(50), nullable=False)
    end_time = db.Column(db.String(50), nullable=False)

    task = db.relationship('Task', backref='event_task', uselist=False)

# Create the database tables
db.create_all()

# Define API routes for CRUD operations
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = []
    for task in tasks:
        task_dict = {
            'id': task.id,
            'type': task.type,
            'description': task.description,
            'done': task.done
        }
        if task.type == 'deadline':
            deadline_task = DeadlineTask.query.filter_by(task_id=task.id).first()
            task_dict['deadline'] = deadline_task.deadline
        elif task.type == 'event':
            event_task = EventTask.query.filter_by(task_id=task.id).first()
            task_dict['start_time'] = event_task.start_time
            task_dict['end_time'] = event_task.end_time
        task_list.append(task_dict)
    return jsonify(task_list)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_type = data['type']
    description = data['description']
    done = data.get('done', False)
    new_task = Task(type=task_type, description=description, done=done)
    db.session.add(new_task)
    
    if task_type == 'deadline':
        deadline = data.get('deadline')
        new_deadline_task = DeadlineTask(task=new_task, deadline=deadline)
        db.session.add(new_deadline_task)
    elif task_type == 'event':
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        new_event_task = EventTask(task=new_task, start_time=start_time, end_time=end_time)
        db.session.add(new_event_task)
    
    db.session.commit()
    
    return jsonify({'message': 'Task created successfully'}), 201

# Implement PATCH and DELETE routes for tasks here

if __name__ == '__main__':
    app.run(debug=True)
