"""
SMARS Lab
Copyright 2019 Kevin McAleer
3 February 2019
Updated 13 June 2021
Updated 15 March 2025
"""

# TODO: add more telemetry - the foot position and ultrasonic distance sensor data

import os
from os import path

import smars_library.smars_library as sl
import yaml
from flask import Flask, render_template, request, jsonify, flash
from flask_bootstrap import Bootstrap
from markupsafe import Markup
from smars_library.smars_library import SmarsRobot
from utils.command_history import CommandHistory

APP = Flask(__name__)
robot = SmarsRobot()

# Comment out the line below to run on without the driver loading
# DRIVER = sl.DO_NOT_USE_PCA_DRIVER

# print(DRIVER)
COMMAND_HISTORY = CommandHistory()
telemetry = []

# Configuration
base_dir = os.getcwd()
config = []
config_file_name = 'smars_lab.yml'
config_file = os.path.join(base_dir, config_file_name)

def load_config():
    """ loads the configuration from the config file - if present """
    my_config = []
    if path.exists(config_file):
        my_config = yaml.load(open(config_file), Loader=yaml.SafeLoader)
        for item in my_config:
            print(f"{item.upper()}: {my_config[item]}")
    else:
        print("No smars_lab.yml configuration file found, using defaults")
    return my_config

@APP.route("/")
def index():
    """ render the main index template """
    global telemetry
    telemetry = robot.get_telemetry()
    if DRIVER:
        flash(Markup('PCA9685 Driver not loaded. For more information visit:'
                     ' <a href="https://kevinmcaleer.github.io/SMARSLab/driver_not_found">This documentation page</a>'), 'danger')
        # flash(Markup('another test of flash'), 'success')
    return render_template("index.html")


@APP.route("/about")
def about():
    """ returns the about page """
    return render_template("about.html")

@APP.route('/metricsapi', methods=['GET', 'POST'])
def metricsapi():
    """ metrics api """
    # print("/metricsapi")
    if request.method == 'POST':
        metric = request.values.get('metric')
        if metric == "telemetry":

            return jsonify(robot.get_telemetry())
    return "Ok"
    # return SMARS.get_telemetry()

# new ControlAPI
@APP.route("/controlapi", methods=['GET', 'POST'])
def controlapi():
    """ control api """
    # print("/ControlAPI hit!")
    if request.method == 'POST':

        # Map commands to corresponding SMARS actions dynamically

        command_actions = {
            "up": lambda: robot.walkforward(steps=10),
            "down": lambda: robot.walkbackward(steps=10),
            "left": lambda: robot.turnleft(),
            "right": lambda: robot.turnright(),
            "stand": lambda: robot.stand(),
            "sit": lambda: robot.sit(),
            "wiggle": lambda: robot.wiggle(wiggle_count=1),
            "clap": lambda: robot.clap(clap_count=1),
            "clear_history": lambda: COMMAND_HISTORY.clear(),
            "home": lambda: robot.default(),
        }

        # Handle "command" and "full_history" edge case
        command = request.values.get('command')
        if command == "full_history":
            return jsonify(COMMAND_HISTORY.get_history())

        # Execute command if its valid
        action = command_actions.get(command)
        if action:
            COMMAND_HISTORY.append(command)
            return jsonify({"status":"success", "command": command})

        # Handle invalid commands
        return jsonify({"status": "error", "message": "Invalid command"}), 400

    return jsonify({"status": "error", "message": "Only POST requests are supported"}), 405


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
    """ shuts down the SMARSLab web server """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@APP.route('/shutdown')
def shutdown():
    """ requests the web server shuts down """
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
        return jsonify(result=f"There was an error {error}")

@APP.route('/telemetry')
def get_telemetry():
    """ return the current telemetry in JSON format """
    return jsonify(telemetry)


@APP.route('/commandhistory', methods=['POST', 'GET'])
def get_command_history():
    """ returns the command history """
    if request.method == 'POST':
        list_type = request.values.get('list_type')
        if list_type == "top10":
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
    # config = load_config()
    APP.secret_key = 'development-key'
    APP.host = '0.0.0.0'
    APP.debug = True
    Bootstrap(APP)
    APP.run(host='0.0.0.0', port=5001)


if __name__ == "__main__":
    main()
