# Kevin McAleer
# June 2021
# Configure SMARS Quad Legs

from smars_library.smars_library import SmarsRobot as SR

quad = SR()

quad.default()


config = quad.config
for item in config:
    print(item['name'], item['channel'])
# print(config)

for item in config:
    print(item['name'], item['invert'])

quad.default()