#!/usr/bin/env python

from modules.hue.hue_remote import parseCommandline
from modules.speech.speech import voiceInput

prefixes = ["computer", "computers"]

class speech_daemon(object):
	voiceInpObj = None

	def __init__(self, deviceIndex=30):
		self.voiceInpObj = voiceInput()
		self.voiceInpObj.setMuted(False)

	def start(self):
		return self.voiceInpObj.start()

if __name__ == "__main__":
	daemon = speech_daemon()

	cmdBuf = None
	for inp in daemon.start():
		cmdBuf = inp.lower().split(" ")
		if( cmdBuf[0] in prefixes ):
			print("CMD:", cmdBuf)
			parseCommandline( cmdBuf[1:], False )
