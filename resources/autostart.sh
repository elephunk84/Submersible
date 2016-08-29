pkill xboxdrv
sudo pkill xboxdrv
sudo rmmod xpad
/usr/local/bin/xboxdrv-daemon.py -v -x /usr/local/bin/xboxdrv --config /home/pi/Submersible/resources/xboxdrv-evdev.conf
/usr/bin/lxterminal -e 'sh /home/pi/Submersible/sub_control_app.sh'
