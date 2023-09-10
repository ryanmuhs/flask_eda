from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

data = pd.read_csv("Tugas Mandiri 080923 - data.csv", index_col="Id")
data_head = data.head()
data_jml_col = len(data.columns)
categories = data.describe()

# data.drop(co)
@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard", kolom=data_jml_col, lot_area = categories)

@app.route("/eda")
def eda():
    return render_template("eda.html", tables=[data_head.to_html(classes="data")], title="Data", kolom=data_jml_col)

@app.route("/predict")
def predict():
    return render_template("predict.html", title="Predict")


if __name__ == "__main__":
    app.run(debug=True)