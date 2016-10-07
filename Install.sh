# Install Dependances
apt-get install python-pip
pip install pyttsx
apt-get install espeak
pip install jupyter
pip install gTTS
apt-get install python-pygame
apt-get install portaudio19-dev
pip install tts-watson
apt-get install python-pyaudio
apt-get install caca-utils
cd /usr/local
wget https://storage.googleapis.com/golang/go1.7.1.linux-amd64.tar.gz
tar -xvf go1.7.1.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go get github.com/ichinaski/pxl
