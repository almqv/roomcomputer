import speech_recognition as sr

class sr_microphone(object):
	recognizer = sr.Recognizer()

	muted = False

	def __init__(self): # use the object as a generator
		while( not muted ):
			try:
				with sr.Microphone() as src:
					recognizer.adjust_for_ambient_noise( src, duration=0.2 ) # adjust for ambient noise

					audio = recognizer.listen(src)

					# Make audio -> text
					return (recognizer.recognize_google( audio )).lower() # use googles recognizer and lower its output

			except sr.RequestError as err:
				print("Unable to request results: {0}".format(e))

			except sr.UnknownValueError:
				print("Unknown Error")

	def setMuted( self, setm: bool=True ):
		self.muted = setm

	def switchMute( self ):
		self.setMuted( not self.muted )
