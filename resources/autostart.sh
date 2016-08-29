pkill xboxdrv
sudo pkill xboxdrv
sudo rmmod xpad
/usr/bin/xboxdrv -D --config /home/pi/Submersible/resources/xboxdrv-evdev.conf --dbus disabled
/usr/bin/lxterminal -e 'sh /home/pi/Submersible/sub_control_app.sh'
