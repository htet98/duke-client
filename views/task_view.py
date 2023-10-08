from flask import Blueprint, request, jsonify
from controllers.task_controller import TaskController

task_view = Blueprint('task_view', __name__)

@task_view.route('/tasks', methods=['GET'])
def get_tasks():
    task_controller = TaskController()
    tasks = task_controller.get_tasks()
    return jsonify(tasks)

@task_view.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_controller = TaskController()
    result, status_code = task_controller.create_task(data)
    return jsonify(result), status_code

# Implement other views (PATCH and DELETE) as needed.
