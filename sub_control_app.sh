#!/bin/bash
THISHOST=$(hostname -f)
case "${THISHOST}" in
    Iains-Laptop)
        BASEDIR='/home/iainstott/GitRepo/Submersible/'
        ;;
    submarine-pi)
        BASEDIR='/home/pi/Submersible/'
        /usr/bin/xterminal sudo xboxdrv --config ./resources/xboxdrv.conf --detach-kernel-driver 
        ;;
esac
cd ${BASEDIR}
pkill xboxdrv >> /dev/null
sudo pkill xboxdrv >> /dev/null
sudo rmmod xpad >> /dev/null
python ./run.py 
# EOF #
