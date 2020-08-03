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

async def API_Request(method: str="GET", params: str="", body: str=""):
    try:
        apiReq = req.Request( method, genUrl(params) ) # initialize the request
        apiReqPrep = apiReq.prepare() # prepair it

        apiReqPrep.body = body # apply the body to the request

        apiSession = req.Session()
        response = apiSession.send(apiReqPrep) # send it to the Hue bridge

        print(response)
        print(response.text)
    except req.exceptions.RequestException as err:
        raise SystemExit(err) # throw the error

async def setLightPower(index: int=1, on: bool=True):
    await API_Request( "PUT", "/lights/" + str(index) + "/state", "{'on':" + boolToString(on) + "}" )

def testReq():
    # loop.run_until_complete( API_Request("GET", "/lights/1") ) # get test

    loop.run_until_complete( setLightPower(1, False) ) # try to turn on/off a light
    loop.close()
