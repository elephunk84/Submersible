#!/bin/bash
git pull
sudo rmmod xpad
sudo xboxdrv --mouse --detach-kernel-driver
python run.py
