#!/bin/bash
pkill xboxdrv
sudo pkill xboxdrv
git pull
sudo rmmod xpad
python run.py &
sudo xboxdrv --config ./resources/xboxdrv.conf --detach-kernel-driver --silent &
