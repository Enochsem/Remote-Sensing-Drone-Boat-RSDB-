#!/usr/bin/python3

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'welcome':"Remote Sensing Drone Boat"}), 200

#SEND READINGS TO CONNECTED DEVICES
@app.route("/sensor_data", methods=['GET'])
def get_sensor_data():
    #query database and return all data
    response = request.get_json()
    return jsonify({"response":response})


#RECEIVE ALL THE SENSOR READING AS ONE JSON OBJECT
@app.route("/sensor_readings", methods=['POST'])
def post_sensor_readings():
    #receive data from device and insert into db
    response = request.get_json()
    return jsonify({"response":"received"}) , 201


@app.route('/login', methods=['POST'])
def loginin():
    pass


@app.route('/register', methods=['POST'])
def register():
    pass


if __name__ == "__main__":
    app.run(debug=True)