import os
from flask import Flask, request, render_template, send_from_directory
from TestRecognizer import classifier

__author__ = 'sourav'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    image_names = os.listdir('./images/output')
    print(image_names)
    return render_template("index.html", image_name="default.png", result = [0,0,0], image_names=image_names)

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/input')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    fn = "out"+filename
    ret = classifier(filename)
    image_names = os.listdir('./images/output')
    print(image_names)
    return render_template("index.html", image_name=fn, result = ret, image_names=image_names)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images/output", filename)

@app.route('/gallery')
def gallery():
    image_names = os.listdir('./images/input')
    for img in image_names:
        os.unlink("./images/input/" + img)
    image_names = os.listdir('./images/output')
    for img in image_names:
        if(img != 'default.png'):
             os.unlink("./images/output/" + img)
    return render_template("index.html", image_name="default.png", result = [0,0,0], image_names=[])

if __name__ == "__main__":
    app.run(host = "192.168.43.167", port=4555, debug=True)
    #app.run(port=4555, debug=True)
