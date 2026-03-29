#!/bin/bash
# Update and install dependencies
apt-get update
apt-get install -y python3-pip git

# Clone git repo
cd /home
git clone https://github.com/m25ai2063-lgtm/vcc3
cd vcc3

# Install python requirements
pip3 install -r requirements.txt

# Run the app in the background
nohup python3 src/app.py > output.log 2>&1 &
