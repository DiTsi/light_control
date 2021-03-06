from flask import Flask, request
import logging
from logging.handlers import TimedRotatingFileHandler
import RPi.GPIO as GPIO


path = 'logs/light.log'
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(path, when='midnight')
logger.addHandler(handler)


class Room:
    def __init__(self, name, pinout):
        self.name = name
        self.pinout = pinout
        self.state = False
        self.setState(self.state)

    def setState(self, state):
        GPIO.setup(self.pinout, GPIO.OUT)
        GPIO.output(self.pinout, state)
        self.state = state

    def toggle(self):
        if self.state:
            self.setState(False)
        else:
            self.setState(True)


application = Flask(__name__)
# you must generate this key with os.urandom(<number>) command
application.config.update(dict(SECRET_KEY="\xaa\xa0\xcbH\xdf\xa0X!\x06u\x16\x014\x12\x87\x1cu7\x833\x83\xd1e\xbb\x00\xf4\x07\x98\xc4Z\x16)\x06{sbx\xc2\xe6\xdc\xda\xb6"))

rooms = {
    "room1": 3,         #4 outOfBox
    "katya": 5,         #3 outOfBox
    "kitchen": 7,       #2 outOfBox
    "corridor1": 8,     #1 outOfBox
    "ditsi": 13,        #5 outOfBox
    "bathroom2": 12,    #6 outOfBox
    "NONE": 11,         #7 outOfBox
    "bathroom1": 10     #8 outOfBox
}
roomsdict = {}

@application.route("/", methods=['GET'])
def root():
    global lights
    global lights_prev
    global roomsdict

    if request.method == 'GET':
        newState = request.args.get('state')
        logger.info('New state: {}'.format(newState))

        state = newState.split(',')
        for p in state:
            rooms, action = p.split('~')
            if rooms == 'all':
                room_list = list(roomsdict.keys())
            else:
                room_list = [rooms]

            for r in room_list:
                if action == 'toggle':
                    roomsdict[r].toggle()
                else:
                    s = True if action == 'on' else False
                    roomsdict[r].setState(s)
                # logger.info('Lights : {}'.format(lights))
    return 'ok'


if __name__ == "__main__":    
    GPIO.setmode(GPIO.BOARD)
    for roomname in rooms.keys():
        roomsdict[roomname] = Room(roomname, rooms[roomname])

    application.run('0.0.0.0', 5002, debug=True)
