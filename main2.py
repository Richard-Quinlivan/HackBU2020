from flask import Flask, render_template, request
import pickle
from DataHolder import DataHolder
# from face_detection.FaceDetectionNN import FaceDetectionNN
# from chatbot.CivicBot import CivicBot
#
#
#
# bot = CivicBot()
# fd = FaceDetectionNN(False)

def addData(sentence):
    from DataHolder import DataHolder
    DataHolder.convo += "<br>" + sentence + "<br>ChatBot: " + "Hello" + "<br>"

def getData():
    from DataHolder import DataHolder
    return DataHolder.convo

app = Flask(__name__)

@app.route("/")

@app.route("/Home.html")
def Home():
    return render_template("Home.html")

@app.route("/face.html")
@app.route("/face", methods=["GET", "POST"])
def face():

    return render_template("face.html")

@app.route("/chat.html")
def chat():
    return render_template("chat.html")

@app.route("/chat", methods=["GET", "POST"])
def getValue():
    input = request.form["input"]
    addData(input)
    return render_template("chat.html", chat = getData())

# @app.route("/question1", methods=["GET", "POST"])
# def getValue1():
#     input = request.form["input"]
#
#     return render_template("question2.html", prevInput1 = input)
#
# @app.route("/question2.html")
# @app.route("/question2", methods=["Get", "POST"])
# def getValue2():
#     prevIn1 = request.form["pInput1"]
#     input = request.form["input"]
#
#     return render_template("question3.html",prevInput1 = prevIn1, prevInput2 = input)
#
# @app.route("/question3.html")
# @app.route("/question3", methods=["GET", "POST"])
# def getValue3():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     input = request.form["input"]
#
#     return render_template("question4.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = input)
#
# @app.route("/question4.html")
# @app.route("/question4", methods=["GET", "POST"])
# def getValue4():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     input = request.form["input"]
#
#     return render_template("question5.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = input)
#
# @app.route("/question5.html")
# @app.route("/question5", methods=["GET", "POST"])
# def getValue5():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#
#     input = request.form["input"]
#
#     return render_template("question6.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = input)
#
# @app.route("/question6.html")
# @app.route("/question6", methods=["GET", "POST"])
# def getValue6():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#
#
#     input = request.form["input"]
#
#     return render_template("question7.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = input)
#
# @app.route("/question7.html")
# @app.route("/question7", methods=["GET", "POST"])
# def getValue7():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#     prevIn6 = request.form["pInput6"]
#
#     input = request.form["input"]
#
#     return render_template("question8.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = prevIn6, prevInput7 = input)
#
# @app.route("/question8.html")
# @app.route("/question8", methods=["GET", "POST"])
# def getValue8():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#     prevIn6 = request.form["pInput6"]
#     prevIn7 = request.form["pInput7"]
#
#     input = request.form["input"]
#
#     return render_template("question9.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = prevIn6, prevInput7 = prevIn7, prevInput8 = input)
#
# @app.route("/question9.html")
# @app.route("/question9", methods=["GET", "POST"])
# def getValue9():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#     prevIn6 = request.form["pInput6"]
#     prevIn7 = request.form["pInput7"]
#     prevIn8 = request.form["pInput8"]
#
#     input = request.form["input"]
#
#     return render_template("question10.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = prevIn6, prevInput7 = prevIn7, prevInput8 = prevIn8, prevInput9 = input)
#
# @app.route("/question10.html")
# @app.route("/question10", methods=["GET", "POST"])
# def getValue10():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#     prevIn6 = request.form["pInput6"]
#     prevIn7 = request.form["pInput7"]
#     prevIn8 = request.form["pInput8"]
#     prevIn9 = request.form["pInput9"]
#
#     input = request.form["input"]
#
#     return render_template("question11.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = prevIn6, prevInput7 = prevIn7, prevInput8 = prevIn8, prevInput9 = prevIn9, prevInput10 = input)
#
# @app.route("/question11.html")
# @app.route("/question11", methods=["GET", "POST"])
# def getValue11():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#     prevIn6 = request.form["pInput6"]
#     prevIn7 = request.form["pInput7"]
#     prevIn8 = request.form["pInput8"]
#     prevIn9 = request.form["pInput9"]
#     prevIn10 = request.form["pInput10"]
#
#     input = request.form["input"]
#
#     return render_template("question12.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = prevIn6, prevInput7 = prevIn7, prevInput8 = prevIn8, prevInput9 = prevIn9, prevInput10 = prevIn10, prevInput11 = input)
#
# @app.route("/question12.html")
# @app.route("/question12", methods=["GET", "POST"])
# def getValue12():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#     prevIn6 = request.form["pInput6"]
#     prevIn7 = request.form["pInput7"]
#     prevIn8 = request.form["pInput8"]
#     prevIn9 = request.form["pInput9"]
#     prevIn10 = request.form["pInput10"]
#     prevIn11 = request.form["pInput11"]
#
#     input = request.form["input"]
#
#     return render_template("question13.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = prevIn6, prevInput7 = prevIn7, prevInput8 = prevIn8, prevInput9 = prevIn9, prevInput10 = prevIn10, prevInput11 = prevIn11, prevInput12 = input)
#
# @app.route("/question13.html")
# @app.route("/question13", methods=["GET", "POST"])
# def getValue13():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#     prevIn6 = request.form["pInput6"]
#     prevIn7 = request.form["pInput7"]
#     prevIn8 = request.form["pInput8"]
#     prevIn9 = request.form["pInput9"]
#     prevIn10 = request.form["pInput10"]
#     prevIn11 = request.form["pInput11"]
#     prevIn12 = request.form["pInput12"]
#
#     input = request.form["input"]
#     print(input)
#
#     return render_template("question14.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = prevIn6, prevInput7 = prevIn7, prevInput8 = prevIn8, prevInput9 = prevIn9, prevInput10 = prevIn10, prevInput11 = prevIn11, prevInput12 = prevIn12, prevInput13 = input)
#
# @app.route("/question14.html")
# @app.route("/question14", methods=["GET", "POST"])
# def getValue14():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#     prevIn6 = request.form["pInput6"]
#     prevIn7 = request.form["pInput7"]
#     prevIn8 = request.form["pInput8"]
#     prevIn9 = request.form["pInput9"]
#     prevIn10 = request.form["pInput10"]
#     prevIn11 = request.form["pInput11"]
#     prevIn12 = request.form["pInput12"]
#     prevIn13 = request.form["pInput13"]
#
#     input = request.form["input"]
#     print(input)
#
#
#     return render_template("question15.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = prevIn6, prevInput7 = prevIn7, prevInput8 = prevIn8, prevInput9 = prevIn9, prevInput10 = prevIn10, prevInput11 = prevIn11, prevInput12 = prevIn12, prevInput13 = prevIn13, prevInput14 = input)
#
# @app.route("/question15.html")
# @app.route("/question15", methods=["GET", "POST"])
# def getValue15():
#     prevIn1 = request.form["pInput1"]
#     prevIn2 = request.form["pInput2"]
#     prevIn3 = request.form["pInput3"]
#     prevIn4 = request.form["pInput4"]
#     prevIn5 = request.form["pInput5"]
#     prevIn6 = request.form["pInput6"]
#     prevIn7 = request.form["pInput7"]
#     prevIn8 = request.form["pInput8"]
#     prevIn9 = request.form["pInput9"]
#     prevIn10 = request.form["pInput10"]
#     prevIn11 = request.form["pInput11"]
#     prevIn12 = request.form["pInput12"]
#     prevIn13 = request.form["pInput13"]
#     prevIn14 = request.form["pInput14"]
#
#     input = request.form["input"]
#
#     return render_template("question15.html",prevInput1 = prevIn1, prevInput2 = prevIn2, prevInput3 = prevIn3, prevInput4 = prevIn4, prevInput5 = prevIn5, prevInput6 = prevIn6, prevInput7 = prevIn7, prevInput8 = prevIn8, prevInput9 = prevIn9, prevInput10 = prevIn10, prevInput11 = prevIn11, prevInput12 = prevIn12, prevInput13 = prevIn13, prevInput14 = prevIn14, prevInput15 = input)
#
#

if __name__ == "__main__":
    app.run(debug=True)
