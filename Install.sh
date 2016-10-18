# What this script is doing spiel
printf "Do you know what this script is doing?\n\nJust checking, but you should really know! This script installs all the dependances required for Multipixelones BlindRemote, and then adds it to startup.\n\nThis will convert your Pi into a talking remote. :)\n\nJust making sure :D\n"

# You sure man?
read -r -p "Are you sure? [y/N] " response
response=${response,,}    # tolower
if [[ $response =~ ^(yes|y)$ ]]
then
    apt-get update
    apt-get --yes --force-yes install python-pip
    pip install pyttsx
    apt-get --yes --force-yes install espeak
    pip install jupyter
    pip install gTTS
    apt-get install --yes --force-yes python-pygame
    apt-get install --yes --force-yes portaudio19-dev
    pip install tts-watson
    apt-get install --yes --force-yes python-pyaudio
    apt-get install --yes --force-yes caca-utils
    apt-get install --yes --force-yes python-picamera
    #cd /usr/local
    #wget https://storage.googleapis.com/golang/go1.7.1.linux-amd64.tar.gz
    #tar -xvf go1.7.1.linux-amd64.tar.gz
    #echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile
    sudo apt-get --yes --force-yes install gccgo-go
    go get github.com/ichinaski/pxl
    pip install schedule
    pip install --upgrade google-api-python-client
else
    echo Install Cancelled... Exiting
    exit 0
fi
