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
sensorKey = ['id','device_id','sensor','value','date']
notificationeys=["id","message","device_id","status","date"]




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


#SEND Specific READINGS TO CONNECTED DEVICES
# requesting data on one sensors only eg:PH
@app.route("/sensor_data", methods=['GET'])
def get_sensor_data():
    column_name = "sensor_type"
    table_name = "sensors"
    data = request.get_json() 
    device_id = data["device_id"]
    #you can perform an authentication 
    sensor_type = data["sensor_type"]
    print("data here1 : ",sensor_type)
    database = Database()
    #query database and return Specific data (where device id is)
    # response = database.select_where(table_name, column_name, sensor_type) 
    single_sensorData = database.select_where2(table_name, "sensor_type", sensor_type, "device_id", device_id)
    response = dbToJson(sensorKey, single_sensorData)
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
    database = Database()
    deviceSensor = DeviceSensor()
    data = request.get_json() 
    if database.check_device_id(device_id):
        print("raw",data)
        database.insert_all_sensor_readings(deviceSensor.toTuple(data, device_id))
        # time.sleep_ms(300)
        #check the thresholds here and insert them into a notification table
        database.checkThreshold(data,device_id=device_id)
        return jsonify({"response":"Received"}) , 201
    return jsonify({"response":"Invalid Request"}) , 401


@app.route('/notification_detail', methods=['POST'])
def notification_detail():
    #update notification status to -1 
    data = request.get_json()
    device_id = data['device_id']
    notification_id = data['notification_id']
    database = Database()
    status = database.update_where2("notification", "status", "-1", "device_id", device_id, "id", notification_id)
    if status:
        notification_data = database.select_where2("notification", "id", notification_id, "device_id", device_id)
        response = dbToJson(notificationeys, notification_data)
        return jsonify({"response":response}) ,200
    return jsonify({"response":"invalid Message ID"}) ,400


@app.route("/notify/<string:device_id>", methods=['GET'])
def notify(device_id):
    table_name = "notification"
    column_name = "device_id"
    database = Database()
    if database.check_device_id(device_id):
        data = database.select_where(table_name, column_name, device_id)
        response = dbToJson(notificationeys, data)
        if len(data) > 0:
            return jsonify({"response":response}) , 200
    return jsonify({"response":"invalid credentials"}) , 401



@app.route("/notification_count/<string:device_id>", methods=['GET'])
def notification_count(device_id):
    table_name = "notification"
    column_name = "device_id"
    database = Database()
    if database.check_device_id(device_id):
        data = database.select_where2(table_name, column_name, device_id, "status", "-1")
        response = len(data)
        if len(data) > 0:
            return jsonify({"response":response}) , 200
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