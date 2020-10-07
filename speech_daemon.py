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
    deviceIndex = 30

    def __init__(self, deviceIndex=30):
        self.voiceInpObj = voiceInput()
        self.voiceInpObj.setMuted(False)

        self.deviceIndex = deviceIndex

    def loadconfig(self):
        path = homedir + "/.config/roomcomputer/config.json"
        # if no config path is
        # specified then choose the users default

        if(len(sys.argv) > 1):
            path = sys.argv[1]

        cfg = readconfig(path)  # read the config

        global CONFIG
        CONFIG = cfg

    def start(self):
        controller.init()

        for inp in self.voiceInpObj.start(self.deviceIndex):
            cmdBuf = inp.lower().split(" ")
            if(cmdBuf[0] in CONFIG["speech"]["prefixes"]):
                print("CMD:", cmdBuf)
                parseCommandline(cmdBuf, False)

        controller.end()


if __name__ == "__main__":
    daemon = speech_daemon()
    daemon.loadconfig()
    daemon.start()
