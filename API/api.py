#!/usr/bin/python3
# import sys
# sys.path.insert(0, 'c:/Users/Enoch/Desktop/RSDB/Project')
from flask import Flask, request, jsonify, abort
from Database.database import Database
from Database.tables import  createDB
from Modules.user import User
from Modules.device import DeviceSensor
from datetime import datetime



app = Flask(__name__)


current_datetime = datetime.now()

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
    table_name = "sensors"
    device_id = request.args.get("device_id")
    #you can perform an authentication 
    sensor_type = request.args.get("sensor_type")
    print("data here1 : ",sensor_type)
    database = Database()
    #query database and return Specific data
    response = database.select_where(table_name, column_name, sensor_type) 
    print(response, "data type ", type(response))
    if len(response) < 0:
        response = "No readings from sensor yet"
        return jsonify({"Error":response}), 301
    return jsonify({"response": response}), 200 


#SEND All READINGS TO CONNECTED DEVICES
@app.route("/sensor_data/<string:device_id>", methods=['GET'])
def sensor_data(device_id):
    table_name = "sensors"
    #query database and return all data
    database = Database()
    response = database.select(table_name)
    if len(response) < 0:
        response = "Device Has Not Taking any Readings"
        return jsonify({"Error":response}), 301
    return jsonify({"response":response}) , 200


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
        
    #check the thresholds here and insert them into a notification table
    Threshold = {
    Ph: 8,
    Turbidity: 150,
    Temperature : 32,
    TDS: 400 
    }

    for d in data['data']:
        for key in Threshold:
            if d == key:
                if data['data'][d] >= Threshold[key]:
                    #insert data 
                    status = database.insert("notification", f"Threshold of {Threshold[key]} reach for {key}", "solution", "1")
    
    return jsonify({"response":"Invalid"}) , 401


@app.route('/login', methods=['POST'])
def login():
    #get user_id and password
    data = request.get_json()
    user_id = data['user_id']
    password = data['password']
    #query db
    database = Database()
    user_data, user_exist = database.signin(user_id, password)
    if user_exist:
        return jsonify(to_user_json(user_data)) , 200
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


@app.route('/notification_detail', methods=['POST'])
def subscription():
    #update notification status to -1 
    data = request.get_json()
    device_id = data['device_id']
    
    database = Database()
    status = database.update("notification", "status", "id", "-1", data["notification_id"])
    if status:
        response = database.select_where("notification", "id", data['notification_id'])
        return jsonify({"response":response}) ,200
        response = "invalid Message ID"
    return jsonify({"response":response}) ,400



@app.route("/notify", methods=['GET'])
def notify():
    ph_threshold = 8
    turbidity_threshold = 0
    tds_threshold = 0
    temperature = 0

    table_name = "notification"
    database = Database()
    data = database.select(table_name)
    if len(data) > 0:
        return jsonify({"response":data}) , 200
    return jsonify({"response":"invalid credentials"}) , 401




def update_client_dashboard():
    # update client dashboard with useful tips to maintain enhace productivity
    pass


def to_user_json(data):
    return {"id":data[0][0],"user_type":data[0][1],"user_id":data[0][2],"device_id":data[0][3]}


#create a json object forset data in sensor type


def forgot_password():
    pass

if __name__ == "__main__":
    app.run(debug=True)