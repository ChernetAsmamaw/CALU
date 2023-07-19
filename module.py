from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint, get_flashed_messages
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_login import UserMixin
from flask_socketio import SocketIO, emit
from datetime import date, datetime
db = SQLAlchemy(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://calu_user:password@localhost/calu'
app.config['SECRET_KEY'] = 'mysecretkey'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    password = db.Column(db.String(128))
    major = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    type = db.Column(db.String(50))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.LargeBinary)
    def set_image(self, filename):
        with open(filename, 'rb') as file:
            self.image = file.read()

    def get_image(self):
        return self.image