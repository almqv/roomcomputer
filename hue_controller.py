import requests as req # Used for HTTP requests for the Hue API
import json # API uses JSON
import config # Configuration for the controller

def genUrl(params: str):
    return "https://" + config.address + "/api/" + config.username + params

def API_Request(ReqType: str, params: str):
    apiReq = req.Request( ReqType, genUrl(params) )

    apiReqPrep = apiReq.prepare()
    apiSession = req.Session()
    apiSession.send(apiReqPrep)


