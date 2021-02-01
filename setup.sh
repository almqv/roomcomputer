#!/usr/bin/bash

cfgPath="$HOME/.config/roomcomputer"

if [ -d $cfgPath ]; then
	echo Config already exists.
else
	mkdir $cfgPath
	cp default-config.json $cfgPath/config.json
	cp default-presets.json $cfgPath/presets.json
fi
