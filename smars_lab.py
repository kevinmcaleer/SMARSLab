"""
SMARS Lab
Copyright 2019 Kevin McAleer
3 February 2019
"""

from flask import Flask, render_template, request, session, redirect, url_for
from models import DB, User
from forms import SignupForm, LoginForm
from SMARS_Library3 import SmarsRobot

APP = Flask(__name__)
SMARS = SmarsRobot()
command_history = ["Initialising Command History"]

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SMARSLABDB.db'
DB.init_app(APP)

APP.secret_key = 'development-key'

@APP.route("/")
def index():
    """ render the main index template """
    return render_template("index.html", command_history=command_history)

@APP.route("/up")
def up():
    """ send up command """
    command_history.append("up")
    SMARS.walkforward(steps=10)
    return render_template("index.html", command_history=command_history)

@APP.route("/down")
def down():
    """ send down command """
    command_history.append("down")
    SMARS.walkbackward(steps=10)
    return render_template("index.html", command_history=command_history)

@APP.route("/left")
def left():
    """ send left command """
    command_history.append("left")
    SMARS.turnleft()
    return render_template("index.html", command_history=command_history)

@APP.route("/right")
def right():
    """ send right command """
    command_history.append("right")
    SMARS.turnright()
    return render_template("index.html", command_history=command_history)

if __name__ == "__main__":
    APP.run(debug=True)
