#!/usr/bin/env python
from lib.input import * # Commandline parser

import hue_controller as hue # Actual controller 

def init():
    hue.testReq()

init()
