from flask import Flask, flash, render_template, redirect, json, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("dashboard.html")


@app.route('/chart')
def chart():
    return render_template("chart.html")



if __name__ == "__main__":
    app.run(debug=True)