#!/bin/bash
THISHOST=$(hostname -f)
echo ${THISHOST}
if [ $THISHOST = "Iains-Laptop" ]; then
    BASEDIR='/home/iainstott/GitRepo/Submersible/'
else if [ $THISHOST = "submarine-pi" ]; then
    BASEDIR='/home/pi/Submersible/'
else
    break
fi
echo ${BASEDIR}
pkill xboxdrv >> /dev/null
sudo pkill xboxdrv >> /dev/null
git pull >> /dev/null
sudo rmmod xpad >> /dev/null
python ${BASEDIR}/run.py &
sudo xboxdrv --config ${BASEDIR}/resources/xboxdrv.conf
fi
# EOF #
