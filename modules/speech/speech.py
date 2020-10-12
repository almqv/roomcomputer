import speech_recognition as sr


class voiceInput(object):
    recognizer = sr.Recognizer()

    muted = True

    # "Error codes", can be used to check stuff
    what = "??"
    error = "ERROR"

    def start(self, deviceIndex=None):  # a generator for everything that is said
        while(True):  # loop
            try:
                if(not self.muted):  # this thing is not the NSA
                    with sr.Microphone(deviceIndex) as src:
                        self.recognizer.adjust_for_ambient_noise(src, 0.2)
                        print("Listening...")
                        audio = self.recognizer.listen(
                            src, phrase_time_limit=5)
                        print("Thinking...")
                        text = self.recognizer.recognize_google(audio)
                        yield text

            except sr.RequestError as err:
                print("Unable to request results: {0}".format(err))
                yield self.error

            except sr.UnknownValueError:
                yield self.what

    def setMuted(self, setm: bool = True):
        self.muted = setm

    def switchMute(self):
        self.setMuted(not self.muted)
