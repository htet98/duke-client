from models.task import Task
from models.deadline_task import DeadlineTask
from models.event_task import EventTask
from app import db

class TaskController:
    def get_tasks(self):
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
        return task_list

    def create_task(self, data):
        try:
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

            return {'message': 'Task created successfully'}, 201
        except Exception as e:
            db.session.rollback()
            return {'error': 'Failed to create task', 'message': str(e)}, 400

    # Implement methods for updating and deleting tasks as needed.
