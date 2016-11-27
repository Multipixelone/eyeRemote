#!/usr/bin/env bash
# What this script is doing
printf "Do you know what this script is doing?\n\nJust checking, but you should really know! This script installs all the dependances required for Multipixelones BlindRemote, and then adds it to startup.\n\nThis will convert your Pi into a talking remote. :)\n\nJust making sure :D\n"

# You sure man?
read -r -p "Proceed with Install? [y/N]"
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]
then
    apt-get update
    apt-get --yes --force-yes upgrade
    raspi-config nonint do_camera 0
    apt-get --yes --force-yes install python-pip
    # pip install pyttsx
    # apt-get --yes --force-yes install espeak
    # pip install jupyter
    pip install gTTS
    apt-get --yes --force-yes install mpg123
    pip install sultan
    apt-get install --yes --force-yes caca-utils
    apt-get install --yes --force-yes python-picamera
    #cd /usr/local
    pip install schedule
    # pip install --upgrade google-api-python-client
    pip install cloudsight
    echo -n "Enter your Cloudsight API Key [ENTER]: "
    read key
    echo "key = '$key'" > LocalVariables.py
    echo -n "Enter the GPIO Pin for Shutdown (BCM) [ENTER]: "
    read -n 3 sdownpin
    echo
    echo "shutdownpin = $sdownpin" >> LocalVariables.py
    echo -n "Enter your GPIO Pin for Take Picture (BCM) [ENTER]: "
    read -n 3 tpicturepin
    echo
    echo "takepicture = $tpicturepin" >> LocalVariables.py
    printf "\n\n\n\n\nInstall Complete!\n Adding to Startup..."
    touch tmpcron
    echo "@reboot python /home/pi/BlindRemote/ShutdownWhenPress.py &" >> tmpcron
    crontab tmpcron
    rm tmpcron
    sleep 2
    printf "\nNow Rebooting...\n"
    sleep 2
    reboot now
else
    echo Install Cancelled... Exiting
    exit 0
fi
