#!/usr/bin/env python

from modules.hue.hue_remote import parseCommand
from modules.speech.speech import voiceInput

class speech_daemon(object):
	voiceInpObj = None

	def __init__(self, deviceIndex=30):
		voiceInpObj = voiceInput()
		voiceInpObj.setMuted(False)

		voiceInpObj.start(deviceIndex)

if __name__ == "__main__":
	daemon = speech_daemon()
