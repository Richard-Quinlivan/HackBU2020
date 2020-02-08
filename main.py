from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/question1.html")
@app.route("/")

def question1():
    return render_template("question1.html")

@app.route("/question1", methods=["POST"])
def getValue():
    # import pdb; pdb.set_trace()
    value = request.form["value"]
    # result = my_model(input=valiue)

    return render_template("question2")

@app.route("/question2", methods=["POST"])
def getValue():
    # import pdb; pdb.set_trace()
    value = request.form["value"]
    # result = my_model(input=valiue)

    return str(value)


if __name__ == "__main__":
    app.run(debug=True)
