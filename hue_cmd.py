#!/usr/bin/env python

from modules.hue.hue_controller import controller
from modules.hue.hue_remote import parseCommandline

def init():
	controller.init() # very important to initialize the controller
	parseCommandline()
	controller.end() # also to end it

if __name__ == "__main__":
	init()
