from models import db, Task

def create_task(title, task_type, due_time=None, start_time=None, end_time=None):
    task = Task(title=title, task_type=task_type, due_time=due_time, start_time=start_time, end_time=end_time)
    db.session.add(task)
    db.session.commit()
    
def get_tasks():
    return Task.query.all()

def mark_task_done(task_id):
    task = Task.query.get(task_id)
    task.done = True
    db.session.commit()

def mark_task_undone(task_id):
    task = Task.query.get(task_id)
    task.done = False
    db.session.commit()

def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
