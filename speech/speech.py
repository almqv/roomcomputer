import speech_recognition as sr
import io
from google.cloud import speech as sp

class voiceInput(object):
	recognizer = sr.Recognizer()
	commandFunc = None

	muted = True

	def transcribe_voice( self, streamFile ):
		cl = sp.SpeechClient()

		with io.open( streamFile, "rb" ) as audioFile:
			cont = audioFile.read()

		stream = [cont]
		req = ( sp.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream )

		conf = sp.RecognitionConfig(
			encoding = sp.RecognitionConfig.AudioEncoding.LINEAR16,
			sample_rate_hertz = 16000,
			language_code = "en-US"
		)


		streamConf = sp.StreamingRecognitionConfig(config=conf)

		responses = cl.streaming_recognize( steamConf, req )

		for res in responses:
			for result in res.results:
				for alt in result.alternatives:
					print(alt.transcript)

	def setMuted( self, setm: bool=True ):
		self.muted = setm

	def switchMute( self ):
		self.setMuted( not self.muted )


vc = voiceInput()
vc.transcribe_voice( "./stream.txt" )
