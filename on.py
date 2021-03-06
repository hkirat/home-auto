import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

def main(args):
    if len(args) < 3:
        sys.exit("Usage: python awesome.py <led> <on/off>")

    pin = int(args[1])
    on = 0

    if args[2] == 'off':
        on = 1

    if args[2] == 'on':
        on = 0

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, on)


if __name__ == '__main__':
    main(sys.argv)