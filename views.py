from flask import render_template, request, redirect, url_for
from controllers import create_task, get_tasks, mark_task_done, mark_task_undone, delete_task

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    create_task(title)
    return redirect(url_for('index'))

@app.route('/done/<int:task_id>')
def done(task_id):
    mark_task_done(task_id)
    return redirect(url_for('index'))

@app.route('/undone/<int:task_id>')
def undone(task_id):
    mark_task_undone(task_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/create_deadline', methods=['POST'])
def create_deadline():
    title = request.form.get('title')
    due_time = request.form.get('due_time')
    create_task(title, 'deadline', due_time=due_time)
    return redirect(url_for('index'))
