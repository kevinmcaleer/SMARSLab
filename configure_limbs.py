# Kevin McAleer
# June 2021
# Configure SMARS Quad Legs

from smars_library.smars_library import SmarsRobot as SR

quad = SR()
config = quad.config

def list_channels():
   for item in config:
    print(item['name'], item['channel'])

def list_invert():
    for item in config:
        print(item['name'], item['invert'])

def identify(channel):
    """ wiggles a limb to identify it """
    quad.identify(channel)

    