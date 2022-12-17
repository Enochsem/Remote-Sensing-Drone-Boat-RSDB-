#https://pypi.org/project/w1thermsensor/

#On the Raspberry Pi, you will need to add dtoverlay=w1-gpio" (for regular connection) 
or dtoverlay=w1-gpio,pullup="y" (for parasitic connection) to your /boot/config.txt. 
The default data pin is GPIO4 (RaspPi connector pin 7), 
but that can be changed from 4 to x with dtoverlay=w1-gpio,gpiopin=x.

After that, don't forget to reboot


1. enadble the on wire interface on the Pi and reboot
2. edit the boot file by typing # sudo nano /boot/config.txt
3. scroll to the bottom and find dtoverlay=wl-gpio  # add  , gpiopin=4
4. sudo pip3 install w1thermsensor #on pi use sudo apt-get install python3-w1thermsensor
