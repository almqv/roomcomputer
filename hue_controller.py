import requests as req # Used for HTTP requests for the Hue API
import json # API uses JSON
import asyncio # ASync stuff

import config # Configuration for the controller (/config.py <- change this file)

LIGHTS = {} # dictionary of all the lights


loop = asyncio.get_event_loop() # ASync loop

def genUrl(params: str):
    return "http://" + config.address + "/api/" + config.username + params

boolStr = {
    True: "true",
    False: "false"
}

StrBool = { # because doing something else is too expensive 
    "true": True,
    "false": False
}

def boolToString(v: bool): # To fix the dumb python syntax
    return boolStr[v]

class APIrequest:
    # Get Req
    async def get( dest: str="", payload: str="" ):
        try:
            apiReq = req.get( genUrl(dest), data = payload )
            return apiReq

        except req.exceptions.RequestException as err:
            print(err)

    # POST Req
    async def post( dest: str="", payload: str="" ):
        try:
            apiReq = req.post( genUrl(params), data = payload )
            return apiReq

        except req.exceptions.RequestException as err:
            print(err)

    # PUT Req
    async def put( dest: str="", payload: str="" ):
        try:
            apiReq = req.put( genUrl(dest), data = payload ) # send the payload
            print(apiReq)
            print(apiReq.text)
            return apiReq

        except req.exceptions.RequestException as err:
            print(err)


class controller:

    # Info
    async def getLights():
        return await APIrequest.get("/lights")

    async def getLight(index: int=1):
        return await APIrequest.get( "/lights/" + str(index) )

    # Lower level light manipulation
    async def toggleLight(index: int=1, isOn: bool=True):
        await APIrequest.put( "/lights/" + str(index) + "/state", '{"on":' + boolToString(isOn) + '}' )

    async def toggleLights(isOn: bool=True):
        for key in LIGHTS:
            await controller.toggleLight(key, isOn)

    # Turning lights on/off
    def switchLight( index: int=1 ):
        key = LIGHTS.get(str(index))
        if(key):
            if( key.get("state") ):
                curPower = LIGHTS[str(index)]["state"]["on"]
                loop.run_until_complete( controller.toggleLight(index, not curPower))
        else:
            print("Error: Light index out of range")

    def switchLights():
        for key in LIGHTS:
            controller.switchLight(key)

    def Power(isOn: bool=True):
        loop.run_until_complete( controller.toggleLights(isOn) )

    # Very important init function
    def init():
        jsonLights = loop.run_until_complete(APIrequest.get("/lights"))
        global LIGHTS
        LIGHTS = json.loads(jsonLights.text)
        print(LIGHTS)
        print("----------------")

def testReq():
    controller.init()
    controller.Power(False) # turn on all lights

    #controller.switchLights()
    # loop.run_until_complete( controller.toggleLight(1, True) ) # try to turn on/off a light

    loop.close()
