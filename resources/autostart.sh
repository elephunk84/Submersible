pkill xboxdrv
sudo pkill xboxdrv
sudo rmmod xpad
/usr/bin/lxterminal -e 'sudo xboxdrv --config /home/pi/Submersible/resources/xboxdrv.conf'
/usr/bin/lxterminal -e 'sh /home/pi/Submersible/sub_control_app.sh'
