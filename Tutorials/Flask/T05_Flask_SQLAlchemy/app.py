import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

path = os.getcwd()

app = Flask(__name__, instance_path=path)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["QLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_joined = db.Column(db.Date, default=datetime.utcnow())

    def __repr__(self):
        return "<User %r>" % self.username
