from flask import Flask, flash, render_template, redirect, json, request, jsonify, session
import requests as api
import json
# from Modules.user import User

app = Flask(__name__)

# app secret key is to help identify the current session
app.secret_key = "@#$%^4535567^%$fghjklkjgfhd@#$%^&*hBGD45"

baseURL = "http://127.0.0.1:5000"


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
                print("response from api",data)
                #set & store data in a session
                session["user_id"]= data['user_id']
                session["device_id"]= data['device_id']
                #session["password"]= data['password']
                return redirect(location='/dashboard')
                
        if request.form['submit'] =='signup':
            user_id = request.form['user_id']
            device_id = request.form['device_id']
            password = request.form['password']
            print(user_id, password)
            #post data to api and await response
            url= baseURL+"/register"
            data= {"user_id":user_id, "device_id":device_id, "password":password}
            response = api.post(url=url, json=data)
            if response.status_code == 201:
                data = response.json()
                print("response from api ",data)
                return redirect(location='/')

    return render_template("index.html")


@app.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")


@app.route('/signup')
def signup():
    data = request.form['userid']
    return "bmnbn"


@app.route('/dashboard')
def dashboard():
    #start a session here
    if not session.get("user_id"):
        return redirect('/')
    #get session data
    user_id = session.get("user_id")
    device_id = session.get("device_id")
    password = session.get("password")
    #get data from api
    url = f"{baseURL}/sensor_data/{device_id}"
    response = api.post(url=url)
    if response.status_code == 200:
        data = response.json()
        print("response from api ",data)
        return redirect(location='/dashboard',data = data)
    
    return render_template("dashboard.html",user_id= user_id,device_id=device_id)


@app.route('/notification')
def notification():
    tresh_hold =3
    return render_template("notification.html")


@app.route('/ph')
def ph():
    return render_template("ph.html")



@app.route('/logout')
def logout():
    session.pop("user_id", default=None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port="5001")