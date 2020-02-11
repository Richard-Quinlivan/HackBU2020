from flask import Flask, render_template, request
from socket import gethostname
import time
import cv2
import pickle
from DataHolder import DataHolder
from face_detection.FaceDetectionNN import FaceDetectionNN
import numpy as np
import glob


# app = Flask(static_folder="/Users/richardquinlivan4444/comp_sci/hackathon/HackBU2020/static", __name__)
app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-store"
    return response


@app.route("/")

@app.route("/Home.html")
def Home():
    DataHolder.reset()
    return render_template("home.html")

@app.route("/face.html")
@app.route("/face", methods=["GET", "POST"])
def face():
    return render_template("face.html")

@app.route("/face2.html")
@app.route("/face2", methods=["GET", "POST"])
def face2():
    cam = cv2.VideoCapture(0)

    time.sleep(1)
    ret, frame = cam.read()

    img_name = "./static/opencv_frame.png"
    cv2.imwrite(img_name, frame)

    cam.release()
    cv2.destroyAllWindows()
    return render_template("face2.html")

@app.route("/face3.html")
@app.route("/face3", methods=["GET", "POST"])
def face3():
    fd = FaceDetectionNN(False)

    saliencyFile = "./static/opencv_frame.png"

    img = cv2.imread(saliencyFile)
    img = cv2.resize(img, (64, 64),interpolation = cv2.INTER_AREA)

    name = "./static/saliency_" + saliencyFile.split('/')[-1]

    fd.showSaliencyMap(img, name)

    prediction = fd.predict(np.asarray([img]))[0]
    index = np.where(prediction == max(prediction))[0][0]

    candidateFiles = sorted(glob.glob("./face_detection/testing/*"))

    result = candidateFiles[index].split('/')[-1]
    path = "../static/" + result + ".jpeg"

    return render_template("face3.html", path = path, name = result)

@app.route("/about.html")
@app.route("/about", methods=["GET", "POST"])
def about():
    DataHolder.reset()
    return render_template("about.html")

@app.route("/question1.html")
def question1():
    DataHolder.reset()
    return render_template("question1.html", prevOutput1 = DataHolder.first)

@app.route("/question1", methods=["GET", "POST"])
def getValue1():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question2.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1])

@app.route("/question2.html")
@app.route("/question2", methods=["Get", "POST"])
def getValue2():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question3.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3])

@app.route("/question3.html")
@app.route("/question3", methods=["GET", "POST"])
def getValue3():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question4.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5])

@app.route("/question4.html")
@app.route("/question4", methods=["GET", "POST"])
def getValue4():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question5.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7])

@app.route("/question5.html")
@app.route("/question5", methods=["GET", "POST"])
def getValue5():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question6.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9])

@app.route("/question6.html")
@app.route("/question6", methods=["GET", "POST"])
def getValue6():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question7.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11])

@app.route("/question7.html")
@app.route("/question7", methods=["GET", "POST"])
def getValue7():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question8.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11], prevInput7 = DataHolder.convo[12], prevOutput8 = DataHolder.convo[13])

@app.route("/question8.html")
@app.route("/question8", methods=["GET", "POST"])
def getValue8():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question9.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11], prevInput7 = DataHolder.convo[12], prevOutput8 = DataHolder.convo[13], prevInput8 = DataHolder.convo[14], prevOutput9 = DataHolder.convo[15])

@app.route("/question9.html")
@app.route("/question9", methods=["GET", "POST"])
def getValue9():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question10.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11], prevInput7 = DataHolder.convo[12], prevOutput8 = DataHolder.convo[13], prevInput8 = DataHolder.convo[14], prevOutput9 = DataHolder.convo[15], prevInput9 = DataHolder.convo[16], prevOutput10 = DataHolder.convo[17])

@app.route("/question10.html")
@app.route("/question10", methods=["GET", "POST"])
def getValue10():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question11.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11], prevInput7 = DataHolder.convo[12], prevOutput8 = DataHolder.convo[13], prevInput8 = DataHolder.convo[14], prevOutput9 = DataHolder.convo[15], prevInput9 = DataHolder.convo[16], prevOutput10 = DataHolder.convo[17], prevInput10 = DataHolder.convo[18], prevOutput11 = DataHolder.convo[19])

@app.route("/question11.html")
@app.route("/question11", methods=["GET", "POST"])
def getValue11():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question12.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11], prevInput7 = DataHolder.convo[12], prevOutput8 = DataHolder.convo[13], prevInput8 = DataHolder.convo[14], prevOutput9 = DataHolder.convo[15], prevInput9 = DataHolder.convo[16], prevOutput10 = DataHolder.convo[17], prevInput10 = DataHolder.convo[18], prevOutput11 = DataHolder.convo[19], prevInput11 = DataHolder.convo[20], prevOutput12 = DataHolder.convo[21])

@app.route("/question12.html")
@app.route("/question12", methods=["GET", "POST"])
def getValue12():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question13.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11], prevInput7 = DataHolder.convo[12], prevOutput8 = DataHolder.convo[13], prevInput8 = DataHolder.convo[14], prevOutput9 = DataHolder.convo[15], prevInput9 = DataHolder.convo[16], prevOutput10 = DataHolder.convo[17], prevInput10 = DataHolder.convo[18], prevOutput11 = DataHolder.convo[19], prevInput11 = DataHolder.convo[20], prevOutput12 = DataHolder.convo[21], prevInput12 = DataHolder.convo[22], prevOutput13 = DataHolder.convo[23])

@app.route("/question13.html")
@app.route("/question13", methods=["GET", "POST"])
def getValue13():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question14.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11], prevInput7 = DataHolder.convo[12], prevOutput8 = DataHolder.convo[13], prevInput8 = DataHolder.convo[14], prevOutput9 = DataHolder.convo[15], prevInput9 = DataHolder.convo[16], prevOutput10 = DataHolder.convo[17], prevInput10 = DataHolder.convo[18], prevOutput11 = DataHolder.convo[19], prevInput11 = DataHolder.convo[20], prevOutput12 = DataHolder.convo[21], prevInput12 = DataHolder.convo[22], prevOutput13 = DataHolder.convo[23], prevInput13 = DataHolder.convo[24], prevOutput14 = DataHolder.convo[25])

@app.route("/question14.html")
@app.route("/question14", methods=["GET", "POST"])
def getValue14():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question15.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11], prevInput7 = DataHolder.convo[12], prevOutput8 = DataHolder.convo[13], prevInput8 = DataHolder.convo[14], prevOutput9 = DataHolder.convo[15], prevInput9 = DataHolder.convo[16], prevOutput10 = DataHolder.convo[17], prevInput10 = DataHolder.convo[18], prevOutput11 = DataHolder.convo[19], prevInput11 = DataHolder.convo[20], prevOutput12 = DataHolder.convo[21], prevInput12 = DataHolder.convo[22], prevOutput13 = DataHolder.convo[23], prevInput13 = DataHolder.convo[24], prevOutput14 = DataHolder.convo[25], prevInput14 = DataHolder.convo[26], prevOutput15 = DataHolder.convo[27])

@app.route("/question15.html")
@app.route("/question15", methods=["GET", "POST"])
def getValue15():
    input = request.form["input"]
    DataHolder.convo.append(input)
    next = DataHolder.getSentence(input)
    if next == "NULL":
        return render_template(DataHolder.findFinal())
    DataHolder.convo.append(next)

    return render_template("question15.html", prevOutput1 = DataHolder.first, prevInput1 = DataHolder.convo[0], prevOutput2 = DataHolder.convo[1], prevInput2 = DataHolder.convo[2], prevOutput3 = DataHolder.convo[3], prevInput3 = DataHolder.convo[4], prevOutput4 = DataHolder.convo[5], prevInput4 = DataHolder.convo[6], prevOutput5 = DataHolder.convo[7], prevInput5 = DataHolder.convo[8], prevOutput6 = DataHolder.convo[9], prevInput6 = DataHolder.convo[10], prevOutput7 = DataHolder.convo[11], prevInput7 = DataHolder.convo[12], prevOutput8 = DataHolder.convo[13], prevInput8 = DataHolder.convo[14], prevOutput9 = DataHolder.convo[15], prevInput9 = DataHolder.convo[16], prevOutput10 = DataHolder.convo[17], prevInput10 = DataHolder.convo[18], prevOutput11 = DataHolder.convo[19], prevInput11 = DataHolder.convo[20], prevOutput12 = DataHolder.convo[21], prevInput12 = DataHolder.convo[22], prevOutput13 = DataHolder.convo[23], prevInput13 = DataHolder.convo[24], prevOutput14 = DataHolder.convo[25], prevInput14 = DataHolder.convo[26], prevOutput15 = DataHolder.convo[27], prevInput15 = DataHolder.convo[28], prevOutput16 = DataHolder.convo[29])



if __name__ == "__main__":
    if 'liveconsole' not in gethostname():
        app.run(debug=True)
