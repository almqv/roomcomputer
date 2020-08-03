import requests as req # Used for HTTP requests for the Hue API
import json # API uses JSON
import config # Configuration for the controller (/config.py <- change this file)

def genUrl(params: str):
    return "http://" + config.address + "/api/" + config.username + params

await def API_Request(ReqType: str="GET", params: str=""): # Requests for the API
    try:
        apiReq = req.Request( ReqType, genUrl(params) )
        apiReqPrep = apiReq.prepare()

        apiSession = req.Session()
        response = apiSession.send(apiReqPrep)

        print(response.body)
    except req.exceptions.RequestException as err:
        raise SystemExit(err) # throw the error


