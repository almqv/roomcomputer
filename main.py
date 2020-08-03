#!/usr/bin/env python
from lib.input import * # Commandline parser

import hue_controller as hue # Actual controller 

params = ""
if( inputHasKeys(["-p"]) ):
    params = getValueOfKey("-p")

reqtype = "GET"
if( inputHasKeys(["-t"]) ):
    reqtype = getValueOfKey("-t")


def init():
    print(reqtype, params)
    hue.API_Request(reqtype, params)

init()
