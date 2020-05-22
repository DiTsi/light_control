from flask import Flask, render_template, request
from light import light
from time import sleep


application = Flask(__name__)
# you must generate this key with os.urandom(<number>) command
application.config.update(dict(SECRET_KEY="\xaa\xa0\xcbH\xdf\xa0X!\x06u\x16\x014\x12\x87\x1cu7\x833\x83\xd1e\xbb\x00\xf4\x07\x98\xc4Z\x16)\x06{sbx\xc2\xe6\xdc\xda\xb6"))


def toggle(saved, index):
    tmp1 = int(saved, 2)^(int(str(10**index), 2))
    tmp2 = bin(tmp1).replace('0b', '')
    return tmp1, tmp2


@application.route("/", methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        if "room" in request.form.keys():
            room_num = int(request.form["room"])
            with open("saved.txt", "r") as f:
                saved = f.read()
            new_light, new_light_string = toggle(saved, room_num)
            with open("saved.txt", "w") as f:
                f.write(new_light_string)
            new_light = chr(new_light)
            light(new_light)
        else:
            room_num = int(request.form["all"])
            if room_num == 1:
                # print("on")
                light("\xff")
                with open("saved.txt", "w") as f:
                    f.write(bin(255).replace('0b', ''))

            elif room_num == 0:
                # print("off")
                light("\x00")
                with open("saved.txt", "w") as f:
                    f.write(bin(0).replace('0b', ''))

            else:
                light("\x10")
                with open("saved.txt", "w") as f:
                    f.write(bin(16).replace('0b', ''))


    if request.method == 'GET':
        tmp = request.args
        if len(tmp):
            eboy = request.args.get('code')
            tmp1 = int(eboy, 2)
            # print("{}".format(tmp1))
            new_light_string2 = chr(tmp1)
            new_light_string_save = bin(tmp1).replace('0b', '')
            light(new_light_string2)
            with open("saved.txt", "w") as f:
                f.write(new_light_string_save)

    return render_template("root.html", title="LIGHT")


# @application.route('/get_toggled_status')
# def toggled_status():
#     current_status = flask.request.args.get('status')
#     if current_status == 'off':
#         print("on")
#         # enable light
#         light(b'\xff')
#     else:
#         print("off")
#         # disable light
#         light(b'\x00')



if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5001"
    application.run(host=host, port=port, debug=True)
