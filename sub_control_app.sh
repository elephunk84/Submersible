#!/bin/bash
THISHOST=$(hostname -f)
if [ $THISHOST = "Iains-Laptop" ]
then
    BASEDIR='/home/iainstott/GitRepo/Submersible/'
if [ $THISHOST = "submarine-pi" ]
then
    BASEDIR='/home/pi/Submersible/'
else
    break
fi
pkill xboxdrv >> /dev/null
sudo pkill xboxdrv >> /dev/null
git pull >> /dev/null
sudo rmmod xpad >> /dev/null
python ${BASEDIR}/run.py &
sudo xboxdrv --config ${BASEDIR}/resources/xboxdrv.conf
fi
# EOF #
