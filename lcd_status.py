#!/usr/bin/python
# Coded with help from: http://makezine.com/projects/build-a-compact-4-node-raspberry-pi-cluster/
import socket
import time
import urllib2
from i2clibraries import i2c_lcd_smbus # https://bitbucket.org/thinkbowl/i2clibraries.git

def internetIsConnected():
    try:
        response = urllib2.urlopen('8.8.8.8', timeout=1)
        return True
    except urllib2.URLError as err: pass
        return False

lcd = i2c_lcd_smbus.i2c_lcd(0x27,1, 2, 1, 0, 4, 5, 6, 7, 3)
lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)
lcd.backLightOn()
lcd.clear()

lcd.writeString("Connecting to")
lcd.setPosition(2,0)
lcd.writeString("Google: 8.8.8.8")

result = internetIsConnected()

if result:
    # TRUE. Display IP.
    while True:
        lcd.clear()
        lcd.setPosition(1,0)
        lcd.writeString("SSH Ready. IP:")
        lcd.setPosition(2,0)
        lcd.writeString([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
        time.sleep(5)
        lcd.clear()
        lcd.setPosition(1,0)
        lcd.writeString("SSH Ready. Host:")
        lcd.setPosition(2,0)
        lcd.writeString(socket.gethostname())
        time.sleep(5)
else:
    while True:
        lcd.clear()
        lcd.setPosition(1,0)
        lcd.writeString("Connection Fail")
        lcd.setPosition(2,0)
        lcd.writeString("   To Google")
        lcd.sleep(5)
        lcd.clear()
        lcd.setPosition(1,0)
        lcd.writeString("Hard Restart pi.")
        lcd.setPosition(2,0)
        lcd.writeString("To reconnect!")
