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
command_history = ["*** Initialising Command History ***"]
telemetry = []

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SMARSLABDB.db'
DB.init_app(APP)

@APP.route("/")
def index():
    """ render the main index template """
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html", command_history=command_history, telemetry=telemetry)

@APP.route("/up")
def up():
    """ send up command """
    command_history.append("up")
    SMARS.walkforward(steps=10)
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html", command_history=command_history, telemetry=telemetry)

@APP.route("/down")
def down():
    """ send down command """
    command_history.append("down")
    SMARS.walkbackward(steps=10)
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html", command_history=command_history, telemetry=telemetry)

@APP.route("/left")
def left():
    """ send left command """
    command_history.append("left")
    SMARS.turnleft()
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html", command_history=command_history, telemetry=telemetry)

@APP.route("/right")
def right():
    """ send right command """
    command_history.append("right")
    SMARS.turnright()
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html", command_history=command_history, telemetry=telemetry)

@APP.route("/stand")
def stand():
    """ send stand command """
    command_history.append("stand")
    SMARS.stand()
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html", command_history=command_history, telemetry=telemetry)

@APP.route("/sit")
def sit():
    """ send sit command """
    command_history.append("sit")
    SMARS.sit()
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html", command_history=command_history, telemetry=telemetry)

@APP.route("/clap")
def clap():
    """ send clap command """
    command_history.append("clap")
    SMARS.clap(1)
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html", command_history=command_history, telemetry=telemetry)

@APP.route("/wiggle")
def wiggle():
    """ send wiggle command """
    command_history.append("wiggle")
    SMARS.wiggle(1)
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html", command_history=command_history, telemetry=telemetry)

def main():
    """ main event loop """
    APP.secret_key = 'development-key'
    APP.run(debug=True, host= '0.0.0.0')

if __name__ == "__main__":
    main()
