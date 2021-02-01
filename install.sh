#!/usr/bin/bash

repoPath=$(dirname "$(realpath $0)")

echo Installing roomcomputer at /opt/...
sudo mkdir -p /opt/roomcomputer
sudo cp -r $repoPath /opt/

echo Linking binaries to /usr/bin/...
sudo ln -s /opt/roomcomputer/hue_cmd.py  /usr/bin/hue

echo Done.
