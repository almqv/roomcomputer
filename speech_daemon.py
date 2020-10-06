#!/usr/bin/env python

from modules.hue.hue_remote import parseCommandline
from modules.hue.hue_controller import controller
from modules.speech.speech import voiceInput

prefixes = ["computer", "computers"]

class speech_daemon(object):
	voiceInpObj = None

	def __init__(self, deviceIndex=30):
		self.voiceInpObj = voiceInput()
		self.voiceInpObj.setMuted(False)

	def start(self):
		controller.init()

		for inp in self.voiceInpObj.start():
			cmdBuf = inp.lower().split(" ")
			if( cmdBuf[0] in prefixes ):
				print("CMD:", cmdBuf)
				parseCommandline( cmdBuf, False )

		controller.end()

if __name__ == "__main__":
	daemon = speech_daemon()
	daemon.start()
