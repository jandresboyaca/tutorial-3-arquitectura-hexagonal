from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = None

def init_db(app: Flask):
    global db
    if db is None:
        db = SQLAlchemy(app)
    else:
        db.init_app(app)