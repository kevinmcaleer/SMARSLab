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


APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SMARSLABDB.db'
DB.init_app(APP)

APP.secret_key = 'development-key'

@APP.route("/")
def index():
    """ render the main index template """
    return render_template("index.html")

@APP.route("/up")
def up():
    """ send up command """
    SMARS.walkforward(steps=10)
    return render_template("index.html")

@APP.route("/down")
def down():
    """ send down command """
    SMARS.walkbackward(steps=10)
    return render_template("index.html")

@APP.route("/left")
def left():
    """ send left command """
    SMARS.turnleft()
    return render_template("index.html")

@APP.route("/right")
def right():
    """ send right command """
    SMARS.turnright()
    return render_template("index.html")

if __name__ == "__main__":
    APP.run(debug=True)
