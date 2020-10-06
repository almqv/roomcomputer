import speech_recognition as sr

class voiceInput(object):
	recognizer = sr.Recognizer()

	muted = True

	def setMuted( self, setm: bool=True ):
		self.muted = setm

	def switchMute( self ):
		self.setMuted( not self.muted )
