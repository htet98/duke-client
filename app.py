from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///duke.db'
db = SQLAlchemy(app)

# Register blueprints for views
from views.task_view import task_view
app.register_blueprint(task_view)

if __name__ == '__main__':
    app.run(debug=True)
