import speech_recognition as sr

class voiceInput(object):
	recognizer = sr.Recognizer()

	muted = True

	def voiceToText( self, deviceIndex=30 ):
		try:
			with sr.Microphone( deviceIndex ) as src:
				self.recognizer.adjust_for_ambient_noise( src, 0.2 )
				print("Listening...")
				audio = self.recognizer.listen( src, phrase_time_limit=5 )
				print("Thinking...")
				text = self.recognizer.recognize_google(audio)
				print(text)

				return self.voiceToText(deviceIndex)

		except sr.RequestError as err:
			print("Unable to request results: {0}".format(err))

		except sr.UnknownValueError as err:
			print("Unknown Error: {0}".format(err))


	def setMuted( self, setm: bool=True ):
		self.muted = setm

	def switchMute( self ):
		self.setMuted( not self.muted )


voice = voiceInput()
voice.setMuted(False)
print( "out:", voice.voiceToText() )
