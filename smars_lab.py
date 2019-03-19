"""
SMARS Lab
Copyright 2019 Kevin McAleer
3 February 2019
"""
# TODO: Replace telemetry and history with jquery dynamic data
# TODO: add more telemetry - the foot position and ultrasonic distance sensor data
# FIXME: create a blank smarslabdb.db, if this is to be usedself.
# TODO: remove the forms.py user login stuff
# TODO: add a smars graphic to the page, depdending on what type is selected.
# TODO: Add smars to pypy

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash
from markupsafe import Markup
from flask_bootstrap import Bootstrap
# from models import DB, User
# from forms import SignupForm, LoginForm
from smars_library.smars_library import SmarsRobot
import smars_library.smars_library
from command_history import CommandHistory

APP = Flask(__name__)
SMARS = SmarsRobot()
DRIVER = smars_library.smars_library.DONOTUSE_PCA_DRIVER
# print(DRIVER)
COMMAND_HISTORY = CommandHistory()
telemetry = []

# TODO: what is this
# APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SMARSLABDB.db'
# DB.init_app(APP)

@APP.route("/")
def index():
    """ render the main index template """
    global telemetry
    telemetry = SMARS.get_telemetry()
    if DRIVER == True:
        flash(Markup('Driver not loaded'), 'danger')
        # flash(Markup('another test of flash'), 'success')
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

@APP.route("/up")
def up():
    """ send up command """
    COMMAND_HISTORY.append("up")
    SMARS.walkforward(steps=10)
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

@APP.route("/down")
def down():
    """ send down command """
    COMMAND_HISTORY.append("down")
    SMARS.walkbackward(steps=10)
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

@APP.route("/left")
def left():
    """ send left command """
    COMMAND_HISTORY.append("left")
    SMARS.turnleft()
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

@APP.route("/right")
def right():
    """ send right command """
    COMMAND_HISTORY.append("right")
    SMARS.turnright()
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

@APP.route("/stand")
def stand():
    """ send stand command """
    COMMAND_HISTORY.append("stand")
    SMARS.stand()
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

@APP.route("/sit")
def sit():
    """ send sit command """
    COMMAND_HISTORY.append("sit")
    SMARS.sit()
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

@APP.route("/clap")
def clap():
    """ send clap command """
    COMMAND_HISTORY.append("clap")
    SMARS.clap(1)
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

@APP.route("/wiggle")
def wiggle():
    """ send wiggle command """
    COMMAND_HISTORY.append("wiggle")
    SMARS.wiggle(1)
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

@APP.route('/clear_history')
def clear_history():
    """ Clear the command history """
    COMMAND_HISTORY.clear()
    global telemetry
    telemetry = SMARS.get_telemetry()
    return render_template("index.html",
                           command_history=COMMAND_HISTORY.history,
                           telemetry=telemetry)

def shutdown_server():
    """ shutsdown the SMARSLab web server """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@APP.route('/shutdown')
def shutdown():
    """ requests the web server shutsdown """
    shutdown_server()
    return 'Server shutting down... Done.'

@APP.route('/background_process')
def background_process():
    """ return dynamic data to JQuery """
    try:
        lang = request.args.get('proglang')
        if str(lang).lower() == 'python':
            return jsonify(result='you are wise')
        else:
            return jsonify(result="try again")
    except Exception as error:
        return(str(error))

@APP.route('/setup')
def setup():
    """ The setup wizard screen """
    if DRIVER == True:
        flash(Markup('Driver not loaded'), 'danger')
        flash(Markup('another test of flash'), 'success')
    return render_template("setup.html")

"""
change up down, forward, left and right into a single endpoint with parameters

"""

@APP.route('/test', methods=['GET','POST'])
def test():
    """ Tests a limb passed to it by a channel number """
    return render_template("setup.html")
def main():
    """ main event loop """
    print("Starting SMARSLab...")
    APP.secret_key = 'development-key'
    APP.host = '0.0.0.0'
    APP.debug = True
    Bootstrap(APP)
    APP.run(host='0.0.0.0')

if __name__ == "__main__":
    main()
