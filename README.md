# SMARSLab

SMARS Lab - A simple web app for playing with SMARS Robots.

To Install:

* log on to your raspberry pi
* clone the SMARS Lab github repository:
 `git clone https://www.github.com/kevinmcaleer/SMARSLab`
* change to the SMARSLab directory:
 `cd SMARSLab`
* install virtualenv:
 `pip install virtualenv`
 or
 'sudo apt-get install virtualenv'
* create a new virtual python environment:
`python3 -m venv venv`
* activate the new python environment:
`source venv/bin/activate`
* install the pre-requisites:
`pip install -r requirements.txt`
* load SMARSLab:
`python smars_lab.py`
* Open a webbrowser at:
either `http://localhost:5000` or `http://raspberrypi-IP-ADDRESS:5000`
* Enjoy!

## ERRATA

- There is an issue with the Walking code at the moment - I'll look at this shortly and apply a fix.
- Had to remove support for Python 3.3 as Flask is not compatible with this version.
- Removed some objc dependencies from requirements.txt as this causes the build to fail

## Arduino Bluetooth control

### Version 1.1

// May 2019 - added buzzer feature
// Requires a Fundomoto sheild

### Version 1.0

* Basic control commands
* known issue with commands not being received correctly
