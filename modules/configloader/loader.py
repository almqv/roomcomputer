import json

def readconfig(path):
	try:
		with open(path) as cfg:
			data = json.load(cfg)

			return data

	except:
		print("[Error] Something went wrong reading the configuration file.")
		print("--", path)
