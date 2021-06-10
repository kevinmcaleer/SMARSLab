---
layout: default
title: Installation
subtitle: How to Install SMARSlab
description: Learn how to install SMARSLab on your Mac, PC or Raspberry Pi
---

![SMARSLab Image](/assets/img/smarslab.png){:class="img-fluid w-25"}

## To Install:

1. log on to your raspberry pi
1. clone the SMARS Lab github repository: `git clone https://www.github.com/kevinmcaleer/SMARSLab`
1. change to the SMARSLab directory: cd SMARSLab
1. install virtualenv: `pip install virtualenv` or `sudo apt-get install virtualenv`
1. create a new virtual python environment: `python3 -m venv venv`
1. activate the new python environment: `source venv/bin/activate`
1. install the pre-requisites: `pip install -r requirements.txt`
1. load SMARSLab: `python smarslab.py`
1. Open a webbrowser at: either `http://localhost:5000` or `http://raspberrypi-IP-ADDRESS:5000`
1. Enjoy!
