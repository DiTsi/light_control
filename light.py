import RPi.GPIO as GPIO
from time import sleep


def low(pin):
    GPIO.output(pin,False)
    sleep(0.01)

def high(pin):
    GPIO.output(pin,True)
    sleep(0.01)

def light_npi(data):
    STCP = 3
    SHCP = 5
    DS = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DS,GPIO.OUT)
    GPIO.setup(SHCP,GPIO.OUT)
    GPIO.setup(STCP,GPIO.OUT)

    low(SHCP)
    low(STCP)
    for i in range(8):
        if data[i]:
            high(DS)
        else:
            low(DS)
        high(SHCP)
        low(SHCP)
    high(STCP)
    low(STCP)
