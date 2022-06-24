from flask import Flask, flash, render_template, redirect, json, request, jsonify, session, url_for
import requests as api
import json
# from Modules.user import User

app = Flask(__name__)

# app secret key is to help identify the current session
app.secret_key = "@#$%^4535567^%$fghjklkjgfhd@#$%^&*hBGD45"

baseURL = "https://rsdbapi.herokuapp.com"
# http://127.0.0.1:5000

@app.route('/',  methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form['submit'] =='signin':
            user_id = str(request.form['user_id'])
            password = str(request.form['password'])
            #post data to api and await response
            url = baseURL+"/login"
            data= {"user_id":user_id, "password":password}
            response = api.post(url=url, json=data)
            if response.status_code == 200:
                data = response.json()
                #return a user object
                # print("response from api",data)
                #set & store data in a session
                session["user_id"]= data['user_id']
                session["device_id"]= data['device_id']
                #session["password"]= data['password']
                return redirect(location='/dashboard')
                
        if request.form['submit'] =='signup':
            user_id = request.form['user_id']
            device_id = request.form['device_id']
            password = request.form['password']
            # print(user_id, password)
            #post data to api and await response
            url= baseURL+"/register"
            data= {"user_id":user_id, "device_id":device_id, "password":password}
            response = api.post(url=url, json=data)
            if response.status_code == 201:
                data = response.json()
                # print("response from api ",data)
                return redirect(location='/')

    return render_template("index.html")



@app.route('/profile')
def profile():
    return render_template("profile.html")




# from here
# home has been changed to index

# @app.route('/home')
# def home():
#     return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
# to here 




@app.route('/dashboard')
def dashboard():
    #start a session check
    if not session.get("user_id"):
        return redirect('/')
    #get session data
    user_id = session.get("user_id")
    device_id = str(session.get("device_id"))
    password = session.get("password")

    return render_template("dashboard.html")


@app.route('/notification')
def notification():
    #start a session here
    if not session.get("user_id"):
        return redirect('/')

    #get data from api
    url = f"{baseURL}/notify"
    response = api.get(url=url)
    if response.status_code == 200:
        data = response.json()
        # print("response from api ",data)
        data_lenght = len(data['response'])
    return render_template("notification.html", notification=data['response'], data_lenght=data_lenght)


@app.route('/notification/<int:notification_id>')
def notification_detail(notification_id):
    # WILL HANDLE THE SOLUTIONS TO THE THRESHOLD LIMITS

    #start a session here
    if not session.get("user_id"):
        return redirect('/')

    device_id = str(session.get("device_id"))
    #get data from api
    url = f"{baseURL}/notification_detail"
    data= {"device_id":device_id, "notification_id":notification_id}
    response = api.post(url=url, json=data)
    if response.status_code == 200:
        data = response.json()
        # print("response from api ",data)
        data_lenght = len(data['response'])
    return render_template("notification_detail.html", detail=data['response'], data_lenght=data_lenght)



@app.route('/ph')
def ph():
     #start a session here
    if not session.get("user_id"):
        return redirect('/')
    #setting the data from api as null as default value
    data = ""
    data_lenght = 0
    #get session data
    user_id = session.get("user_id")
    device_id = str(session.get("device_id"))
    password = session.get("password")
    
    #get data from api
    url = f"{baseURL}/sensor_data"
    params = {"device_id": device_id, "sensor_type":"Ph"}
    response = api.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # print("response from api ",data)
        data_lenght = len(data['response'])
    return render_template("ph.html",data=data['response'], data_lenght=data_lenght)




@app.route('/turbidity')
def turbidity():
     #start a session here
    if not session.get("user_id"):
        return redirect('/')
    #setting the data from api as null as default value
    data = ""
    data_lenght = 0
    #get session data
    user_id = session.get("user_id")
    device_id = str(session.get("device_id"))
    password = session.get("password")
    
    #get data from api
    url = f"{baseURL}/sensor_data"
    params = {"device_id": device_id, "sensor_type":"Turbidity"}
    response = api.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # print("response from api ",data)
        data_lenght = len(data['response'])
    return render_template("turbidity.html",data=data['response'], data_lenght=data_lenght)



@app.route('/tds')
def tds():
     #start a session here
    if not session.get("user_id"):
        return redirect('/')
    #setting the data from api as null as default value
    data = ""
    data_lenght = 0
    #get session data
    user_id = session.get("user_id")
    device_id = str(session.get("device_id"))
    password = session.get("password")
    
    #get data from api
    url = f"{baseURL}/sensor_data"
    params = {"device_id": device_id, "sensor_type":"TDS"}
    response = api.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # print("response from api ",data)
        data_lenght = len(data['response'])
    return render_template("tds.html",data=data['response'], data_lenght=data_lenght)



@app.route('/temperature')
def temperature():
     #start a session here
    if not session.get("user_id"):
        return redirect('/')
    #setting the data from api as null as default value
    data = ""
    data_lenght = 0
    #get session data
    user_id = session.get("user_id")
    device_id = str(session.get("device_id"))
    password = session.get("password")
    
    #get data from api
    url = f"{baseURL}/sensor_data"
    params = {"device_id": device_id, "sensor_type":"Temperature"}
    response = api.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # print("response from api ",data)
        data_lenght = len(data['response'])
    return render_template("temperature.html",data=data['response'], data_lenght=data_lenght)



@app.route('/custom')
def custom():
    #start a session here
    if not session.get("user_id"):
        return redirect('/')
    #setting the data from api as null as default value
    data = ""
    #get session data
    user_id = session.get("user_id")
    device_id = str(session.get("device_id"))
    password = session.get("password")
    
    #get all data from api
    url = f"{baseURL}/sensor_data/{device_id}"
    response = api.get(url=url)
    if response.status_code == 200:
        data = response.json()
        # print("response from api ",data)
        data_lenght = len(data['response'])
    return render_template("custom.html",all_data = data['response'], data_lenght=data_lenght)



@app.route("/get_graph_data", methods=['GET'])
def get_graph_data():
    device_id = request.args.get("device_id")
    sensor_type = request.args.get("sensor_type")
    url = f"{baseURL}/sensor_data"
    params = {"device_id": device_id, "sensor_type":sensor_type}
    response = api.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # print("response from api ",data)
    return data


@app.route("/all_graph_data", methods=['GET'])
def all_graph_data():
    device_id = request.args.get("device_id")
    #get all data from api
    url = f"{baseURL}/sensor_data/{device_id}"
    response = api.get(url=url)
    if response.status_code == 200:
        data = response.json()
        # print("response from api ",data)
    return data


@app.route('/logout')
def logout():
    session.pop("user_id", default=None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port="5001")