from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.create_all()
