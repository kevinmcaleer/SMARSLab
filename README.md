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
`virtualenv -p python3 venv`
* activate the new python environment:
`source venv/bin/activate`
* install the pre-requisites:
`pip install -r requirements.txt`
* load SMARSLab:
`python smarslab.py`
* Open a webbrowser at:
either `http://localhost:5000` or `http://raspberrypi-IP-ADDRESS:5000`
* Enjoy!
