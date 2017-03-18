import RPi.GPIO as GPIO
import sys
from gpiozero import LED, Button

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

def main(args):
    if len(args) < 3:
        sys.exit("Usage: python awesome.py <led> <on/off>")

    pin = int(args[1])
    on = 0

    led1 = LED(pin)
    if args[2] == 'on':
        led1.on();

    if args[2] == 'off':
        led1.off();

if __name__ == '__main__':
    main(sys.argv)