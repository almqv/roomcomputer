#!/usr/bin/bash

cfgPath="$HOME/.config/roomcomputer"

mkdir $cfgPath
cp default-config.json $cfgPath/config.json
cp default-presets.json $cfgPath/presets.json
