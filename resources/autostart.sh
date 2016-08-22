pkill xboxdrv
sudo pkill xboxdrv
sudo rmmod xpad
cd /home/pi/Submersible; find . -name "*.pyc" -type f -delete; git pull
/usr/bin/lxterminal -e 'sudo xboxdrv --config /home/pi/Submersible/resources/xb$
/bin/sleep 15
/usr/bin/lxterminal -e 'sh /home/pi/Submersible/sub_control_app.sh'
