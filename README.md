# Room-Computer
Room-Computer is a simple room controller and is basically a controller for your gadgets. *This is a work-in-progress* so keep in mind that more features will be added in the future. Check the [feature list](#features) to view all of the current supported things and stuff.

### Installation
	git clone https://github.com/E-Almqvist/roomcomputer.git
	pip install -r requirements.txt

### Setup and Configuration
Run the `setup.sh` script in order to copy the necessary files to `~/.config/roomcomputer/`. If you are planning to create a service for the `speech_daemon.py` with systemd; then you can specify its configuration file as the first argument: `speech_daemon.py /path/to/config/config.json`.

#### HUE Lights presets
You can create presets in the `~/.config/roomcomputer/presets.json` file. Follow this syntax *(and JSON syntax of course)*:
```json
{
	"mypreset": {
		"color": [178, 199, 255], # RGB, from 0-255
		"brightness": 100 # from 0-255
	},
}
```
	

### Usage
#### HUE Remote
	--Help page--
	'hue' : Display this help page
	'hue light (index)' ... : Specify light target, from 1-3
	'hue lights' ... : Specify all lights

	--Commands--
	'on'/'off' : Turn light(s) on/off
	'switch' : Switch the light(s) power
	'set ...'
		'preset (preset ID)' : Set the preset (from presets.py)
		'color (red) (green) (blue)' : Set the color, from 0-255
		'brightness (brightness)' : Set the brightness, from 0-255

	Examples:
	'hue light 2 on' : Turn on light 2
	'hue lights set color 255 255 255' : Set all lights colors to white

-----------------
For convenience, you can create an alias for the script file. Append this to your shells rc file:
`alias hue="/path/to/the/cloned/repo/hue_cmd.py"`

<h3 id="features">Features</h3>

* HUE Light Controller (command-line) `hue_cmd.py)`
* HUE Light Controller (voice daemon) `speech_daemon.py`
 
 And more to come!
