from flask import Flask, request
from light import light_npi as light


application = Flask(__name__)
# you must generate this key with os.urandom(<number>) command
application.config.update(dict(SECRET_KEY="\xaa\xa0\xcbH\xdf\xa0X!\x06u\x16\x014\x12\x87\x1cu7\x833\x83\xd1e\xbb\x00\xf4\x07\x98\xc4Z\x16)\x06{sbx\xc2\xe6\xdc\xda\xb6"))

lights = [0, 0, 0, 0, 0, 0, 0, 0]
lights_prev = [0, 0, 0, 0, 0, 0, 0, 0]

roomsdict = {
    # "corridor1": 
    # "corridor2": 
    "kitchen": 1,
    "bathroom1": 7,
    "bathroom2": 5,
    "katya:": 2,
    "dmitry": 4,
    "ditsi": 4
    # "parents": 
    # "irina": 
    # "sergey": 
}

def toggle(saved, index):
    tmp1 = int(saved, 2)^(int(str(10**index), 2))
    tmp2 = bin(tmp1).replace('0b', '')
    return tmp1, tmp2


@application.route("/", methods=['GET'])
def root():
    global lights
    global lights_prev

    if request.method == 'GET':
        room = request.args.get('room')
        action = request.args.get('action') # on, off, toggle
        
        lights = lights_prev
        if action == 'on':
            lights[roomsdict[room]] = 1
        elif action == 'off':
            lights[roomsdict[room]] = 0
        elif action == 'toggle':
            lights[roomsdict[room]] = lights[roomsdict[room]] ^ 1
        else:
            print('Incorrect action')
        light(lights)
        lights_prev = lights

    return 'ok'


if __name__ == "__main__":
    application.run('0.0.0.0', 5002, debug=True)
