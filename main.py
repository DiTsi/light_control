from flask import Flask, request
from light import light_npi as light


application = Flask(__name__)
# you must generate this key with os.urandom(<number>) command
application.config.update(dict(SECRET_KEY="\xaa\xa0\xcbH\xdf\xa0X!\x06u\x16\x014\x12\x87\x1cu7\x833\x83\xd1e\xbb\x00\xf4\x07\x98\xc4Z\x16)\x06{sbx\xc2\xe6\xdc\xda\xb6"))

lights = [0, 0, 0, 0, 0, 0, 0, 0]
lights_prev = [0, 0, 0, 0, 0, 0, 0, 0]
roomsdict = {
    "corridor1": 7,
    # "corridor2": 
    "kitchen": 6,
    "bathroom1": 0,
    "bathroom2": 2,
    "katya": 5,
    "dmitry": 3,
    "ditsi": 3
    # "parents": 
    # "irina": 
    # "sergey": 
}


@application.route("/", methods=['GET'])
def root():
    global lights
    global lights_prev
    global roomsdict

    if request.method == 'GET':
        room = request.args.get('room')
        action = request.args.get('action') # on, off, toggle
        
        room = room.split(",")
        lights = lights_prev
        for r in room:
            if action == 'on':
                lights[roomsdict[r]] = 1
            elif action == 'off':
                lights[roomsdict[r]] = 0
            elif action == 'toggle':
                lights[roomsdict[r]] = lights[roomsdict[r]] ^ 1
            else:
                print('Incorrect action')
        light(lights)
        lights_prev = lights

    return 'ok'


if __name__ == "__main__":
    application.run('0.0.0.0', 5002, debug=True)
