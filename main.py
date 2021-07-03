from flask import Flask, request
from light import light_npi as light
import logging
from logging.handlers import TimedRotatingFileHandler


path = 'logs/light.log'
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(path, when='midnight')
logger.addHandler(handler)

application = Flask(__name__)
# you must generate this key with os.urandom(<number>) command
application.config.update(dict(SECRET_KEY="\xaa\xa0\xcbH\xdf\xa0X!\x06u\x16\x014\x12\x87\x1cu7\x833\x83\xd1e\xbb\x00\xf4\x07\x98\xc4Z\x16)\x06{sbx\xc2\xe6\xdc\xda\xb6"))

lights = [0, 0, 0, 0, 0, 0, 0, 0]
lights_prev = [0, 0, 0, 0, 0, 0, 0, 0]
roomsdict = {
    "corridor1": 7,
    "kitchen": 6,
    "bathroom1": 0,
    "bathroom2": 2,
    "katya": 5,
    "dmitry": 3,
    "ditsi": 3
}


def set_state(roomname, action):
    global lights
    global roomsdict

    if action == 'on':
        lights[roomsdict[roomname]] = 1
    elif action == 'off':
        lights[roomsdict[roomname]] = 0
    elif action == 'toggle':
        lights[roomsdict[roomname]] = lights[roomsdict[roomname]] ^ 1
    else:
        logger.info('Incorrect action: {}'.format(action))
    

@application.route("/", methods=['GET'])
def root():
    global lights
    global lights_prev
    global roomsdict

    if request.method == 'GET':
        newState = request.args.get('state')
        logger.info('New state: {}'.format(newState))

        state = newState.split(',')
        for pos in state:
            room, action = pos.split('~')
            if room == 'all':
                room_list = list(roomsdict.keys())
            else:
                room_list = [room]
            for r in room_list:
                set_state(r, action)
        light(lights)
        logger.info('Lights : {}'.format(lights))
        lights_prev = lights

    return 'ok'


if __name__ == "__main__":
    application.run('0.0.0.0', 5002, debug=True)
