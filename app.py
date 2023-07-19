from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint, get_flashed_messages
from models import app, User, db


@app.route('/')
def index():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)