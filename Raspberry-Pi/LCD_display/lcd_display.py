#!/usr/bin/python
from RPi import GPIO
from RPLCD.gpio import CharLCD
import time
#from RPLCD import CharLCD

# Setup display
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35,
              pins_data=[40, 38, 36, 32, 33, 31, 29, 23],
	      numbering_mode=GPIO.BOARD,
	      dotsize=8,
              charmap='A02',
              auto_linebreaks=True)

lcd.write_string('hello\r\n world')
time.sleep(5)
lcd.clear()
