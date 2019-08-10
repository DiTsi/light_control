import serial
from time import sleep
# from binascii import hexlify, unhexlify


def light(data):
    ser = serial.Serial (
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        xonxoff=serial.XOFF,
        rtscts=False,
        dsrdtr=False
    )

    if not ser.isOpen():
        ser.open()

    sleep(0.5)
    ser.write(data)
