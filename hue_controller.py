import requests as req # Used for HTTP requests for the Hue API
import json # API uses JSON
import asyncio # ASync stuff
import config # Configuration for the controller (/config.py <- change this file)

loop = asyncio.get_event_loop() # ASync loop

def genUrl(params: str):
    return "http://" + config.address + "/api/" + config.username + params

def boolToString(v: bool): # To fix the dumb python syntax
    if(v):
        return "true"
    else:
        return "false"

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
    async def getLights():
        return await APIrequest.get("/lights")

    async def getLight(index: int=1):
        return await APIrequest.get( "/lights/" + str(index) )

    async def toggleLight(index: int=1, isOn: bool=True):
        await APIrequest.put( "/lights/1/state", '{"on":' + boolToString(isOn) + '}' )

def testReq():
    loop.run_until_complete( controller.toggleLight(1, True) ) # try to turn on/off a light

    loop.close()
