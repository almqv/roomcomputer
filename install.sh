#!/usr/bin/bash

repoPath=$(dirname "$(realpath $0)")

echo Creating roomcomputer symlink in /opt/...
sudo ln -s $repoPath /opt/roomcomputer
sudo pip install -r /opt/roomcomputer/requirements.txt

echo Creating hue_cmd.py symlink in /usr/bin/...
sudo ln -s /opt/roomcomputer/hue_cmd.py  /usr/bin/hue

echo Done.
