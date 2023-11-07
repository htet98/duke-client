from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# File path for storing task data
DATA_FILE = 'tasks.txt'

# Initialize the tasks list by reading data from the file
tasks = []

def read_tasks_from_file():
    try:
        with open(DATA_FILE, 'r') as file:
            lines = file.readlines()
            for line in lines:
                task_info = line.strip().split('|')
                description = task_info[0]
                deadline = task_info[1] if len(task_info) > 1 else ''
                start_time = task_info[2] if len(task_info) > 2 else ''
                end_time = task_info[3] if len(task_info) > 3 else ''
                done = task_info[-1] == 'done'
                task = {
                    'description': description,
                    'deadline': deadline,
                    'start_time': start_time,
                    'end_time': end_time,
                    'done': done
                }
                tasks.append(task)
    except FileNotFoundError:
        pass

# Save tasks to the data file
def save_tasks_to_file():
    with open(DATA_FILE, 'w') as file:
        for task in tasks:
            task_info = f"{task['description']}|{task['deadline']}|{task['start_time']}|{task['end_time']}|{'done' if task['done'] else 'undone'}\n"
            file.write(task_info)

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

        task = {
            'description': description,
            'deadline': deadline,
            'start_time': start_time,
            'end_time': end_time,
            'done': False
        }
        tasks.append(task)
        save_tasks_to_file()

        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit_task/<int:task_index>', methods=['GET', 'POST'])
def edit_task(task_index):
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]

        if request.method == 'POST':
            description = request.form['description']
            deadline = request.form['deadline']
            start_time = request.form['start_time']
            end_time = request.form['end_time']

            task['description'] = description
            task['deadline'] = deadline
            task['start_time'] = start_time
            task['end_time'] = end_time
            save_tasks_to_file()

            return redirect(url_for('index'))

        return render_template('edit_task.html', task=task)

    return redirect(url_for('index'))

@app.route('/mark_done/<int:task_index>')
def mark_done(task_index):
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        task['done'] = True
        save_tasks_to_file()

    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_index>')
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks_to_file()

    return redirect(url_for('index'))

if __name__== '__main__':
    read_tasks_from_file()
    app.run(debug=True)
