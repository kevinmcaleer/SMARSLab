"""
SMARS Lab
Copyright 2019 Kevin McAleer
3 February 2019
Updated 13 June 2021 
"""
# TODO: add more telemetry - the foot position and ultrasonic distance sensor data
# FIXME: create a blank smarslabdb.db, if this is to be usedself.
# TODO: add a smars graphic to the page, depdending on what type is selected.

# import bluetooth
from flask import Flask, render_template, request, jsonify, flash
from markupsafe import Markup
from flask_bootstrap import Bootstrap
# from models import DB, User
# from forms import SignupForm, LoginForm
from smars_library.smars_library import SmarsRobot
import os
from os import path 
import yaml

import smars_library.smars_library as sl
from command_history import CommandHistory

APP = Flask(__name__)
SMARS = SmarsRobot()
# SMARS.invert_feet()
DRIVER = sl.DO_NOT_USE_PCA_DRIVER

# print(DRIVER)
COMMAND_HISTORY = CommandHistory()
telemetry = []

# TODO: what is this
# APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SMARSLABDB.db'
# DB.init_app(APP)

# Configuration
base_dir = os.getcwd()
config = []
config_file_name = 'smars_lab.yml'
config_file = os.path.join(base_dir, config_file_name)

def load_config():
    """ loads the configuration from the config file - if present """
    config = []
    if path.exists(config_file):
        config = yaml.load(open(config_file), Loader=yaml.SafeLoader)
        for item in config:
            print(f"{item.upper()}: {config[item]}")
    else:
        print("No smars_lab.yml configuration file found, using defaults")
    return (config)


@APP.route("/")
def index():
    """ render the main index template """
    global telemetry
    telemetry = SMARS.get_telemetry()
    if DRIVER == True:
        flash(Markup('PCA9685 Driver not loaded. For more information visit: <a href="https://kevinmcaleer.github.io/SMARSLab/driver_not_found">This documentation page</a>'), 'danger')
        # flash(Markup('another test of flash'), 'success')
    return render_template("index.html")


@APP.route("/about")
def about():
    """ returns the about page """
    return render_template("about.html")

@APP.route("/blockly")
def blockly():
    return render_template("blockly.html")

@APP.route('/metricsapi', methods=['GET', 'POST'])
def metricsapi():
    """ metrics api """
    # print("/metricsapi")
    if request.method == 'POST':
        metric = request.values.get('metric')
        if metric == "telemetry":

            return jsonify(SMARS.get_telemetry())
    return "Ok"
    # return SMARS.get_telemetry()

# new ControlAPI
@APP.route("/controlapi", methods=['GET', 'POST'])
def controlapi():
    """ control api """
    # print("/ControlAPI hit!")
    if request.method == 'POST':
        command = request.values.get('command')
        if command == "up":
            COMMAND_HISTORY.append("up")
            SMARS.walkforward(steps=10)
        if command == "down":
            COMMAND_HISTORY.append("down")
            SMARS.walkbackward(steps=10)
        if command == "left":
            COMMAND_HISTORY.append("left")
            SMARS.turnleft()
        if command == "right":
            COMMAND_HISTORY.append("right")
            SMARS.turnright()
        if command == "stand":
            COMMAND_HISTORY.append("stand")
            SMARS.stand()
        if command == "sit":
            COMMAND_HISTORY.append("sit")
            SMARS.sit()
        if command == "wiggle":
            COMMAND_HISTORY.append("wiggle")
            SMARS.wiggle(1)
        if command == "clap":
            COMMAND_HISTORY.append("clap")
            SMARS.clap(1)
        if command == "clear_history":
            COMMAND_HISTORY.clear()
        if command == "full_history":
            return jsonify(COMMAND_HISTORY.get_history())
        if command == "home":
            COMMAND_HISTORY.append("home")
            SMARS.default()

    return "Ok"


@APP.route('/bluetooth')
def bluetooth():
    """ shows the bluetooth detection page """
    return render_template("bluetooth.html")


@APP.route('/bluetoothapi', methods=['GET', 'POST'])
def bluetooth_api():
    """ Bluetooth endpoint """
    if request.method == 'POST':
        command = request.values.get('command')
        if command == "up":
            COMMAND_HISTORY.append("up")
        if command == "down":
            COMMAND_HISTORY.append("down")
        if command == "detect":
            print("Detecting devices")
            nearby_devices = bluetooth.discover_devices(
                lookup_names=True, flush_cache=True, duration=10)
            for addr, name in nearby_devices:
                print(" %s - %s" % (addr, name))
            return jsonify(nearby_devices)
    return "Ok"


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
        
#         return(str(error))
        return jsonify(result="There was an error")


@APP.route('/telemetry')
def get_telemetry():
    """ return the current telemetry in JSON format """
    return jsonify(telemetry)


@APP.route('/commandhistory', methods=['POST', 'GET'])
def get_command_history():
    """ returns the command history """
    if request.method == 'POST':
        listtype = request.values.get('listtype')
        if listtype == "top10":
            return jsonify(COMMAND_HISTORY.get_last_ten())
        else:
            return jsonify(COMMAND_HISTORY.get_history())
    """ return the current command history in JSON format """
    return jsonify(COMMAND_HISTORY.get_history())


@APP.route('/setup')
def setup():
    """ The setup wizard screen """
    if DRIVER is True:
        flash(Markup('Driver not loaded'), 'danger')

    return render_template("setup.html")


"""
change up down, forward, left and right into a single endpoint with parameters

"""


@APP.route('/test', methods=['GET', 'POST'])
def test():
    """ Tests a limb passed to it by a channel number """
    return render_template("setup.html")


def main():
    """ main event loop """
    print("Starting SMARSLab...")
    config = load_config()
    APP.secret_key = 'development-key'
    APP.host = '0.0.0.0'
    APP.debug = True
    Bootstrap(APP)
    APP.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
