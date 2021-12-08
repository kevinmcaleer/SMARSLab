# Servo Configuration Tool for SMARS Quad

import smars_library.smars_library as sl

leg = sl.Leg(name= "front left leg", channel=0, leg_minangle=9, leg_maxangle=90, invert= True)
print(f"Setting {leg.name} to default position")
leg.default()
