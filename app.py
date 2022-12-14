from flask import Flask, render_template, request, redirect
import pickle
import sklearn
import numpy as np
import pandas as pd

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":

        with open("random_forest", "rb") as r:
            model = pickle.load(r)

        Pregnancies = float(request.form["melahirkan"])
        Glucose = float(request.form["glukosa"])
        BloodPressure = float(request.form["darah"])
        SkinThickness = float(request.form["kulit"])
        Insulin = float(request.form["insulin"])
        bmi = float(request.form["bmi"])
        DiabetesPedigreeFunction = float(request.form["riwayat"])
        Age = float(request.form["umur"])

        datas = np.array((Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, bmi, DiabetesPedigreeFunction, Age))
        datas = np.reshape(datas, (1, -1))

        predikDiabet = model.predict(datas)

        return render_template("done.html", HasilData=predikDiabet)

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)