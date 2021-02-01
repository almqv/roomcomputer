#!/usr/bin/bash

repoPath=$(dirname "$(realpath $0)")

# Setup config stuff
$repoPath/setup.sh


# Install the stuff
echo Creating roomcomputer symlink in /opt/...
sudo rm /opt/roomcomputer 
sudo ln -s $repoPath /opt/roomcomputer
sudo pip install -r /opt/roomcomputer/requirements.txt

echo Creating hue_cmd.py symlink in /usr/bin/...
sudo rm /usr/bin/hue
sudo ln -s /opt/roomcomputer/hue_cmd.py /usr/bin/hue

echo Done.
