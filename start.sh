#!/bin/bash
cd /home/pi/eyeRemote
sleep 3s
python /home/pi/eyeRemote/ShutdownWhenPress.py &
python /home/pi/eyeRemote/start.py
