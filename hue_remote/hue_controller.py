import requests as req # Used for HTTP requests for the Hue API
import json # API uses JSON
import asyncio # ASync stuff
import time

from lib.func import * # useful functions

import config # Configuration for the controller (/config.py <- change this file)
from presets import * # presets for the lights

LIGHTS = {} # dictionary of all the lights

loop = asyncio.get_event_loop() # ASync loop

def genUrl(params: str):
	return "http://" + config.address + "/api/" + config.username + params

class APIrequest:
	# Get Req
	async def get( dest: str="", payload: str="" ):
		try:
			apiReq = req.get( genUrl(dest), data = payload )

			if( apiReq.status_code != 200 ): # print out the error if the status code is not 200
				print(apiReq)
				print(apiReq.text)

			return apiReq

		except req.exceptions.RequestException as err:
			print(err)

	# PUT Req
	async def put( dest: str="", payload: str="" ):
		try:
			apiReq = req.put( genUrl(dest), data = payload ) # send the payload

			if( apiReq.status_code != 200 ):
				print(apiReq)
				print(apiReq.text)

			return apiReq

		except req.exceptions.RequestException as err:
			print(err)


class controller:

	# Internal get functions
	async def getLights():
		return await APIrequest.get("/lights")

	async def getLight(index: int=1):
		return await APIrequest.get( "/lights/" + str(index) )

	# Lower level light manipulation (async)
	async def toggleLight(index: int=1, isOn: bool=True):
		await APIrequest.put( "/lights/" + str(index) + "/state", '{"on":' + boolToString(isOn) + '}' )

	async def toggleLights(isOn: bool=True):
		for key in LIGHTS:
			await controller.toggleLight(key, isOn)

	async def setLightRGB( index: int, r:int, g:int, b:int ):
		h, s, v = rgbToHsv(r, g, b)
		payload = '{"sat":' + str(s) + ', "bri":' + str(v) + ', "hue":' + str(h) + '}'

		await APIrequest.put( "/lights/" + str(index) + "/state", payload )

	# Normal functions
	def switchLight( index: int=1 ):
		key = LIGHTS.get(str(index))
		if(key):
			if( key.get("state") ):
				curPower = LIGHTS[str(index)]["state"]["on"]
				loop.run_until_complete( controller.toggleLight(index, not curPower))
		else:
			print("Error: Light index '" + str(index) + "' out of range")

	def switchLights():
		for key in LIGHTS:
			controller.switchLight(key)

	# Light control
	def setLightColor( index:int, r:int, g:int, b:int ):
		if( LIGHTS.get(str(index)) ):
			loop.run_until_complete( controller.setLightRGB(index, r, g, b) )
		else:
			print("Error: Light index '" + str(index) + "' out of range")

	def setLightBrightness( index:int, b:int ):
		if( LIGHTS.get(str(index)) ):
			payload = '{"bri":' + str(b) + '}'
			loop.run_until_complete( APIrequest.put( "/lights/" + str(index) + "/state", payload ) )
		else:
			print("Error: Light index '" + str(index) + "' out of range")

	def setBrightness( b:int ):
		for key in LIGHTS:
			controller.setLightBrightness( key, b )

	def setAllLightsColor( r:int, g:int, b:int ):
		for key in LIGHTS:
			controller.setLightColor( key, r, g, b )

	def Power(isOn:bool=True): # Controlling the power of the lights
		loop.run_until_complete( controller.toggleLights(isOn) )

	def powerLight( index:int, isOn:bool=True ):
		loop.run_until_complete( controller.toggleLight( index, isOn ) )

	# Presets
	def setLightPreset( index:int, p:str ):
		if( LIGHTS.get(str(index)) ):
			if( PRESETS.get(p) ):
				preset = PRESETS[p]
				r, g, b = preset["color"]
				brightness = preset["brightness"]

				controller.setLightColor( index, r, g, b )
				controller.setLightBrightness( index, brightness )
			else:
				print("Error: Unknown preset '" + p + "'")
		else:
			print("Error: Light index '" + str(index) + "' out of range")

	def setPreset( presetID:str, index:int=-1 ):
		if( PRESETS.get(presetID) ):
			if( index == -1 ):
				for key in LIGHTS:
					controller.setLightPreset( key, presetID )
			else:
				controller.setLightPreset( index, presetID )
		else:
			print("Error: Unknown preset '" + presetID + "'")

	def countLights():
		return len(LIGHTS)

	# Controller "system" functions
	def delay(n:int):
		time.sleep(n)

	def init():
		jsonLights = loop.run_until_complete(APIrequest.get("/lights"))

		global LIGHTS
		LIGHTS = json.loads(jsonLights.text)

	def end():
		loop.close()
