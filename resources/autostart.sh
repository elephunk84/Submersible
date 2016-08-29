pkill xboxdrv
sudo pkill xboxdrv
sudo rmmod xpad
screen -dm -S Xbox 'sudo xboxdrv --config /home/pi/Submersible/resources/xboxdrv-evdev.conf'
/usr/bin/lxterminal -e 'sh /home/pi/Submersible/sub_control_app.sh'
