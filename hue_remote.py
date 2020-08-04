#!/usr/bin/env python
from lib.input import * # Commandline parser

import hue_controller as hue # Actual controller 

cmd = "hue"

def help():
    print("--Help page--")

    print( "'" + cmd + "' : Display this help page" )
    print( "'" + cmd + " light (index)' ... : Specify light target" )
    print( "'" + cmd + " lights' ... : Specify all lights\n" )

    print("--Commands--")
    print( "'on/off' : Turn light(s) on/off" )
    print( "'set ...'" )
    print( "    'preset (preset ID)' : Set the preset (from presets.py)" )
    print( "    'color (red) (green) (blue)' : Set the color, from 0-255" )
    print( "    'brightness (brightness)' : Set the brightness, from 0-255" )

    print("\nExamples:\n'hue light 2 on' : Turn on light 2\n'hue lights set color 255 255 255' : Set all lights colors to white")

help()
