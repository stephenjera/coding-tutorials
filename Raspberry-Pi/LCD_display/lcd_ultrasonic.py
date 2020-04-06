#!/usr/bin/python

#https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
#Libraries
import RPi.GPIO as GPIO
import time
#from RPi import GPIO
from RPLCD.gpio import CharLCD


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

#set GPIO Pins
GPIO_TRIGGER = 21
GPIO_ECHO = 19

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Setup display
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35,
              pins_data=[40, 38, 36, 32, 33, 31, 29, 23],
              numbering_mode=GPIO.BOARD,
              dotsize=8,
              charmap='A02',
              auto_linebreaks=True)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.2f cm" % dist)
            lcd.write_string("dist %d cm" % dist)
            time.sleep(1)
            lcd.clear()

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
