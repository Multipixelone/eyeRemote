# eyeRemote (formerly BlindRemote)
Yep, This is code that runs on Raspberry Pi that uses the [CloudSight](http://www.cloudsightapi.com/ "Cloudsight API") image recognition API to tell blind people what they are looking at! This README Will be updated as time goes on, this is pretty bare-bones so far.

## Downloading and Installing
Clone the Repository and Run Install Script:
```bash
cd ~
sudo git clone https://github.com/Multipixelone/eyeRemote.git
cd ~/eyeRemote
sudo ./Install.sh
```
## [Optional] Force audio to come out of Headphone Jack (For using a small speaker)
Run this command:
```bash
amixer cset numid=3 1
```

Enjoy your remote!
