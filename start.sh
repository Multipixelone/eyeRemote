#!/bin/bash
cd /home/pi/eyeRemote
#sleep 3s
python /home/pi/eyeRemote/ShutdownWhenPress.py & > /home/pi/eyeRemote/logs/shutdown.log
python /home/pi/eyeRemote/start.py & > /home/pi/eyeRemote/logs/start.log
