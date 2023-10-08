from flask import Flask
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///duke.db'  # SQLite3 database file
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
