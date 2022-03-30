#!/usr/bin/python3
# import sys
# sys.path.insert(0, 'c:/Users/Enoch/Desktop/RSDB/Project')
from flask import Flask, request, jsonify, abort
from Database.database import Database
from Database.tables import  createDB
from Modules.user import User
from Modules.device import DeviceSensor



app = Flask(__name__)


# @app.before_request
# def accept_json():
#     if not request.is_json: 
#         abort(400) 


@app.route("/")
def index():
    return jsonify({'welcome':"Remote Sensing Drone Boat"}), 200


#SEND Specific READINGS TO CONNECTED DEVICES
# requesting data on one sensors only eg:PH
@app.route("/sensor_data", methods=['GET'])
def get_sensor_data():
    column_name = "sensor_type"
    data = request.get_json()
    table_name = data["device_id"]
    database = Database()
    #query database and return Specific data
    response = database.select_where(table_name, column_name, data["sensor_type"]) 
    # device_id = data_request['device_id']
    if len(response) < 0:
        response = "No readings from sensor yet"
        return response
    return jsonify({"response":response}) #create a json response object for response


#SEND All READINGS TO CONNECTED DEVICES
@app.route("/sensor_data/<string:device_id>", methods=['GET'])
def sensor_data(device_id):
    table_name = device_id
    #query database and return all data
    database = Database()
    response = database.select(table_name)
    if device_id == "":
        response = "Device Id Not Found"
        return response
    return jsonify({"response":response})

#RECEIVE ALL THE SENSOR READING AS ONE JSON OBJECT
@app.route("/sensor_readings", methods=['POST'])
def post_sensor_readings():
    #receive data from device and insert into db
    data = request.get_json()
    database = Database()
    device_sensor = DeviceSensor(data["device_id"], data["sensor_type"], data["sensor_reading"])
    status = database.insert_readings(device_sensor)
    if status:
        return jsonify({"response":"received"}) , 201
    return jsonify({"response":"Invalid"}) , 401


@app.route('/login', methods=['POST'])
def loginin():
    #get user_id and password
    data = request.get_json()
    user_id = data['user_id']
    password = data['password']
    #query db
    database = Database()
    user_data, user_exist = database.signin(user_id, password)
    if user_exist:
        return jsonify({"response":to_user_json(user_data)}) , 200
    return jsonify({"response":"invalid user credentials"}) , 401


@app.route('/register', methods=['POST'])
def register():
    user_type = "CLIENT"
    database = Database()
    #get user_id and password
    data = request.get_json()
    user_id = data['user_id']
    device_id = str(data['device_id'])
    password = data['password']
    print("in api", device_id)
    user = User(user_type, user_id, device_id, password)
    #query db
    registered = database.signup(user)
    if registered:
        return jsonify({"response":"Account Created"}) , 201
    return jsonify({"response":"invalid credentials"}) , 401


@app.route('/subscription', methods=['POST'])
def subscription():
    #update users table with subscription type
    data = request.get_json()
    subscription_type = data["subscription_type"]
    device_id = data['device_id']
    
    database = Database()
    database.update_subscription(subscription_type, device_id)
    #get payment/ transaction id to validate payment
    return jsonify({"response":"subscription updated"})


def update_client_dashboard():
    # update client dashboard with useful tips to maintain enhace productivity
    pass


def to_user_json(data):
    return {"id":data[0][0],"user_type":data[0][1],"user_id":data[0][2],"device_id":data[0][3]}


def forgot_password():
    pass

if __name__ == "__main__":
    app.run(debug=True)