#!/usr/bin/python3
from flask import Flask, request, jsonify, abort
# from flask_httpauth import HTTPBasicAuth
from Database.database import Database
from Database.tables import  createDB
from Modules.user import User
from Modules.device import DeviceSensor
from datetime import datetime



app = Flask(__name__)
# auth = HTTPBasicAuth()


current_datetime = datetime.now()



# @auth.verify_password
# def authenticate(user_id, password):
#     if user_id and password:
#         database = Database()
#         user_data, user_exist = database.signin(user_id, password)
#         if user_exist:
#             return jsonify(to_user_json(user_data)) , 200
#         else:
#             return False
#     else:
#         return False



# @app.before_request
# def accept_json():
#     if not request.is_json: 
#         abort(400) 

 
@app.route("/")
# @auth.login_required
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
    column_name = "device_id"
    sensorKey = ['id','device_id','sensor','value','date']
    #query database and return all data
    database = Database()
    if database.check_device_id(device_id):
        data = database.select_where(table_name, column_name, device_id)
        response = dbToJson(sensorKey, data)
        if len(response) < 0:
            response = "Device Has Not Taking any Readings"
        return jsonify({"response":response}) , 200
    return jsonify({"Error":"Invalid Device ID"}), 301
    

#RECEIVE ALL THE SENSOR READING AS ONE JSON OBJECT
@app.route("/sensor_readings/<string:device_id>", methods=['POST']) 
def post_sensor_readings(device_id):
    #receive data from device and insert into db
    data = request.get_json() 
    if database.check_device_id(device_id):
        print("raw",data)
        database = Database()
        deviceSensor = DeviceSensor()
        database.insert_all_sensor_readings(deviceSensor.toTuple(data, device_id))
        return jsonify({"response":"Received"}) , 201
    #check the thresholds here and insert them into a notification table
    deviceSensor.checkThreshold(data)
    return jsonify({"response":"Invalid Request"}) , 401


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
    # print("in api", device_id)
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
    return jsonify({"response":"invalid Message ID"}) ,400



@app.route("/notify/<string:device_id>", methods=['GET'])
def notify(device_id):
    table_name = "notification"
    column_name = "device_id"
    database = Database()
    if database.check_device_id(device_id):
        data = database.select_where(table_name, column_name, device_id)
        if len(data) > 0:
            return jsonify({"response":data}) , 200
    return jsonify({"response":"invalid credentials"}) , 401


def to_user_json(data):
    return {"id":data[0][0],"user_type":data[0][1],"user_id":data[0][2],"device_id":data[0][3]}

def sensorObject(sensorData):
    sensorKey = ['id','device_id','sensor','value','date']
    return [dict(zip(sensorKey, data)) for data in sensorData]

def dbToJson(keyList,listOfTuple):
    return [dict(zip(keyList, data)) for data in listOfTuple]


if __name__ == "__main__":
    app.run(debug=True)