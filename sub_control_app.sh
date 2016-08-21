#!/bin/bash
THISHOST=$(hostname -f)
case "${THISHOST}" in
    Iains-Laptop)
        BASEDIR='/home/iainstott/GitRepo/Submersible/'
        ;;
    submarine-pi)
        BASEDIR='/home/pi/Submersible/'
        ;;
esac
cd ${BASEDIR}
find . -name "*.pyc" -type f -delete
git pull
pkill xboxdrv
sudo pkill xboxdrv
sudo rmmod xpad
python ./run.py  
sudo xboxdrv --config ./resources/xboxdrv.conf
# EOF #
