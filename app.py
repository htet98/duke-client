from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id_counter = 1

class Task:
    def __init__(self, description: str, deadline: str=None, start_time: str=None, end_time: str=None, done: bool=False):
        self.id = task_id_counter
        self.description = description
        self.deadline = deadline
        self.start_time = start_time
        self.end_time = end_time
        self.done = done
        task_id_counter += 1

# Routes for the task manager
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        description = request.form['description']
        deadline = request.form['deadline']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        task = Task(description, deadline, start_time, end_time)
        tasks.append(task)

        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)

    if not task:
        return redirect(url_for('index'))

    if request.method == 'POST':
        description = request.form['description']
        deadline = request.form['deadline']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        task.description = description
        task.deadline = deadline
        task.start_time = start_time
        task.end_time = end_time

        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)

@app.route('/mark_done/<int:task_id>')
def mark_done(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)

    if task:
        task.done = True

    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)

    if task:
        tasks.remove(task)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
