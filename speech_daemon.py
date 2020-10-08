#!/usr/bin/env python

import sys

from modules.hue.hue_remote import parseCommandline
from modules.hue.hue_controller import controller
from modules.speech.speech import voiceInput

from modules.configloader.loader import readconfig

from os.path import expanduser
homedir = expanduser("~")

CONFIG = {}

class speech_daemon(object):
	voiceInpObj = None
	deviceIndex = None

	def __init__(self):
		self.voiceInpObj = voiceInput()
		self.voiceInpObj.setMuted(False)

	def loadconfig(self):
		path = homedir + "/.config/roomcomputer/config.json"
		# if no config path is 
		# specified then choose the users default

		if( len(sys.argv) > 1 ):
			path = sys.argv[1]

		cfg = readconfig(path) # read the config

		global CONFIG
		CONFIG = cfg

		self.deviceIndex = CONFIG["speech"]["device_index"] # Apply the device index

	def start(self):
		controller.init()

		for inp in self.voiceInpObj.start( self.deviceIndex ):
			if( inp != self.voiceInpObj.error and inp != self.voiceInpObj.what ):
				cmdBuf = inp.lower().split(" ")
				if( cmdBuf[0] in CONFIG["speech"]["prefixes"] ):
					print("CMD:", cmdBuf)
					parseCommandline( cmdBuf, False )
			else:
				print("Error/What: {0}".format(inp))

		controller.end()

if __name__ == "__main__":
	daemon = speech_daemon()
	daemon.loadconfig()
	daemon.start()
