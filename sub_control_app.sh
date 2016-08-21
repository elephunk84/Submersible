#!/bin/bash
THISHOST=$(hostname -f)
echo ${THISHOST}
case "${THISHOST}" in
    Iains-Laptop)
        BASEDIR='/home/iainstott/GitRepo/Submersible/'
        ;;
    submarine-pi)
        BASEDIR='/home/pi/Submersible/'
        ;;
esac
echo ${BASEDIR}
pkill xboxdrv >> /dev/null
sudo pkill xboxdrv >> /dev/null
git pull >> /dev/null
sudo rmmod xpad >> /dev/null
python ${BASEDIR}/run.py &
sudo xboxdrv --config ${BASEDIR}/resources/xboxdrv.conf
# EOF #
