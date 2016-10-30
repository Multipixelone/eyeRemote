#!/usr/bin/env bash
# What this script is doing
printf "Do you know what this script is doing?\n\nJust checking, but you should really know! This script installs all the dependances required for Multipixelones BlindRemote, and then adds it to startup.\n\nThis will convert your Pi into a talking remote. :)\n\nJust making sure :D\n"

# You sure man?
read -r -p "Proceed with Install? [y/N]"
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Nn]$ ]]
then
    apt-get update
    apt-get upgrade
    apt-get --yes --force-yes install python-pip
    # pip install pyttsx
    # apt-get --yes --force-yes install espeak
    # pip install jupyter
    pip install gTTS
    apt-get install --yes --force-yes python-pygame
    apt-get install --yes --force-yes portaudio19-dev
    # pip install tts-watson
    apt-get install --yes --force-yes python-pyaudio
    apt-get install --yes --force-yes caca-utils
    apt-get install --yes --force-yes python-picamera
    #cd /usr/local
    #wget https://storage.googleapis.com/golang/go1.7.1.linux-amd64.tar.gz
    #tar -xvf go1.7.1.linux-amd64.tar.gz
    #echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile
    #sudo apt-get --yes --force-yes install gccgo-go
    #go get github.com/ichinaski/pxl
    pip install schedule
    # pip install --upgrade google-api-python-client
    pip install cloudsight
    printf "\n\n\n\n\nInstall Complete!\n Adding to Startup..."
    # Add program to startup
    sleep 5
    printf "\nNow Running Program...\n"
    sleep 2
    python start.py
else
    echo Install Cancelled... Exiting
    exit 0
fi
