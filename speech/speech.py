import speech_recognition as sr

class sr_microphone(object):
	recognizer = sr.Recognizer()

	muted = True

	def start(self): # use the object as a generator
		while( not self.muted ):
			try:
				with sr.Microphone() as src:
					self.recognizer.adjust_for_ambient_noise( src, duration=0.2 ) # adjust for ambient noise

					audio = self.recognizer.listen(src)

					# Make audio -> text
					return (self.recognizer.recognize_google( audio )).lower() # use googles recognizer and lower its output

			except sr.RequestError as err:
				print("Unable to request results: {0}".format(err))

			except sr.UnknownValueError as err:
				print("Unknown Error: {0}".format(err))

	def setMuted( self, setm: bool=True ):
		self.muted = setm

	def switchMute( self ):
		self.setMuted( not self.muted )


# Small test
voice = sr_microphone()
voice.setMuted(False)
voice.start()
