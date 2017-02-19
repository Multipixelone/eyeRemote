#!/usr/bin/env bash
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root. Try running the command with 'sudo' preceding it" 1>&2
    exit 1
fi
# What this script is doing
printf "Do you know what this script is doing?\n\nJust checking, but you should really know! This script installs all the dependances required for Multipixelones eyeRemote, and then adds it to startup.\n\nThis will convert your Pi into a talking remote. :)\n\nJust making sure :D\n A working internet is REQUIRED on first install\n"

# You sure?
read -r -p "Proceed with Install? [y/N]"
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]
then
    apt-get update
    apt-get --yes --force-yes upgrade
    raspi-config nonint do_camera 0
    apt-get --yes --force-yes install python-pip
    pip install gTTS
    apt-get --yes --force-yes install mpg123
    pip install sultan
    apt-get install --yes --force-yes caca-utils
    apt-get install --yes --force-yes python-picamera
    pip install schedule
    pip install cloudsight
    echo -n "Enter your Cloudsight API Key [ENTER]: "
    read key
    echo "key = '$key'" > LocalVariables.py
    echo -n "Enter your Cloudsight secret key [ENTER]: "
    read secret
    echo "secret = '$secret'" >> LocalVariables.py
    echo -n "Enter the GPIO Pin for shutting down the Pi (BCM) [ENTER]: "
    read sdownpin
    echo
    echo "shutdownpin = $sdownpin" >> LocalVariables.py
    echo -n "Enter your GPIO Pin for taking a picture (BCM) [ENTER]: "
    read tpicturepin
    echo
    echo "takepicture = $tpicturepin" >> LocalVariables.py
    printf "\n\n\n\n\nInstall Complete!\n Adding to Startup..."
    sed -i '1i./home/pi/eyeRemote/start.sh &' /etc/rc.local
    sleep 1
    printf "\nNow Rebooting...\n"
    sleep 1
    reboot now
else
    echo Install Cancelled... Exiting
    exit 0
fi
