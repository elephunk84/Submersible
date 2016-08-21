#!/bin/bash
pkill xboxdrv >> /dev/null
sudo pkill xboxdrv >> /dev/null
git pull >> /dev/null
sudo rmmod xpad >> /dev/null
python run.py &
sudo xboxdrv --config ./resources/xboxdrv.conf
