# from flask import Flask, render_template, send_file, request
# from forms import SearchForm
import flask
from flask import Flask, render_template, request
from light import light


application = Flask(__name__)
# you must generate this key with os.urandom(<number>) command
application.config.update(dict(SECRET_KEY="\xaa\xa0\xcbH\xdf\xa0X!\x06u\x16\x014\x12\x87\x1cu7\x833\x83\xd1e\xbb\x00\xf4\x07\x98\xc4Z\x16)\x06{sbx\xc2\xe6\xdc\xda\xb6"))


@application.route("/", methods=['POST', 'GET'])
def root():
    # form = SearchForm()
    # status = ""
    # if request.method == "POST":

    #
    # if request.method == 'POST':
    #     print(request.form.getlist("hello"))
    #
    # return render_template("root.html")
    # if form.validate_on_submit():
    #     text = request.form.get("text")
    #     area_list = request.form.getlist("cities")
    #
    #     if not form.subm.data:
    #         pass
    #         # some_var = some_func()
    #         # status = "some_var: {}".format(some_var)
    #     else:
    #         # save_file(filename)
    #         return send_file("./file.txt", as_attachment=True)
    return render_template("root.html", title="Search")
    # return render_template("root.html", form=form, title="Search", message=status)


@application.route('/get_toggled_status')
def toggled_status():
    current_status = flask.request.args.get('status')
    if current_status == 'off':
        print("on")
        # enable light
        light(b'\xff')
    else:
        print("off")
        # disable light
        light(b'\x00')


    return 'on' if current_status == 'off' else 'off'


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    application.run(host=host, port=port, debug=True)