from flask import Flask, render_template, url_for
import pandas as pd
import numpy as np

app = Flask(__name__)

data = pd.read_csv("Tugas Mandiri 080923 - data.csv", index_col="Id")
data_col = data.columns.tolist()
data_val = data.values.tolist()
data_dict = data.to_dict(orient="records")
data_jml_col = len(data.columns)
categories = data.describe()
lot_area = (sum([row['LotArea'] for row in data_dict]))

# data.drop(co)
@app.route("/")
@app.route("/dashboard")
def dashboard():
    sum_harga = (sum([row['SalePrice'] for row in data_dict]))
    avg_harga = sum_harga / len(data_dict)
    return render_template("dashboard.html", title="Dashboard", jml_col=data_jml_col, lot_area=lot_area, kolom=data.columns.tolist(), avg_harga="{:,.2f}".format(avg_harga))

@app.route("/eda")
def eda():
    return render_template("eda.html", tables=data_dict, title="Data", jml_col=data_jml_col, columns=data_col, values=data_val)

@app.route("/predict")
def predict():
    return render_template("predict.html", title="Predict")


if __name__ == "__main__":
    app.run(debug=True)