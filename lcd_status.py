#!/usr/bin/python
# Coded with help from: http://makezine.com/projects/build-a-compact-4-node-raspberry-pi-cluster/
import socket
from i2clibraries import i2c_lcd_smbus # https://bitbucket.org/thinkbowl/i2clibraries.git

def getIPAddress(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd = i2c_lcd_smbus.i2c_lcd(0x27,1, 2, 1, 0, 4, 5, 6, 7, 3)

lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)
lcd.backLightOn() #TODO: Change this so that the LCD-Backlight isn't just on all the time.

lcd.writeString("IP ")
lcd.writeString(getIPAddress('eth0')) #TODO: Set this to the name for the Wi-Fi adapter

lcd.setPosition(2, 0)
lcd.writeString("BrennanPi Ready")
