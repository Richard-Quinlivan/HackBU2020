from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/question1.html")
@app.route("/question2.html")
@app.route("/question3.html")

@app.route("/")

def question1():
    return render_template("question1.html")

@app.route("/question1", methods=["GET", "POST"])
def getValue1():
    value = request.form["value"]

    return render_template("question2.html")

@app.route("/question2", methods=["Get", "POST"])
def getValue2():
    value = request.form["value"]

    return render_template("question3.html")

@app.route("/question3", methods=["GET", "POST"])
def getValue3():
    value = request.form["value"]

    return str(value)

if __name__ == "__main__":
    app.run(debug=True)
