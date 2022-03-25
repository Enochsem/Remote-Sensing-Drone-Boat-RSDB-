import sqlite3
import datetime




class DataBase():
    DATABASE_NAME = "RSDB.db"
    USERS_TABLE = "users"
    DEVICES_TABLE = "devices"

    current_datetime = datetime.datetime.now()

    def __init__(self):
        self.connection = sqlite3.connect(self.DATABASE_NAME)
        self.cursor = self.connection.cursor()


    def signup(self,user):
        user_type = 'client'
        _user = user
        isregistered = self.check_device_id(_user.device_id)    #check if device exist/ is registered
        if isregistered:
            self.cur.execute(f"INSERT INTO {USERS_TABLE}('user_type','user_id', 'device_id', 'password')VALUES(?,?,?,?)", 
            (_user.user_type, _user.user_id, _user.device_id, _user.password))
            self.con.commit()
            #insert data into client db
            return True
        return False


    def signin(self, user,user_id,password):
        self.cur.execute("SELECT * FROM users WHERE user_id=? AND password=?", (user_id,password))
        data = self.cur.fetchall()
        if len(data) > 0:
            #user_type = data[0][1]
            # print(data)
            return data
        return False


    def insert_readings(self,sensor_data,dynamic_table_name):
        sensor = sensor_data
        #insert data from the sensors
        self.cur.execute(f"INSERT INTO {dynamic_table_name}('sensor','reading','datetime')VALUES(?,?,?)",
        (sensor.sensor_type,sensor.reading,current_datetime))
        self.con.commit()
        return True
        

    def select(self,table_name):
        self.cur.execute(f"SELECT * FROM {table_name}")
        data = self.cur.fetchall()
        return data

    def select_where(self,table_name,column_name,data):
        self.cur.execute(f"SELECT * FROM {table_name} WHERE {column_name}=?", (data,))
        data = self.cur.fetchall()
        return data


    def ispresent(self,table_name,column_name,data):
        self.cur.execute(f"SELECT * FROM {table_name} WHERE {column_name}=?", (data,))
        data = self.cur.fetchall()
        return len(data) > 0


    def check_device_id(self, device_id):
        #check if manufacturer has device or a client has already registered with the device id
        column = "device_id"
        isregistered = self.ispresent(USERS_TABLE, column, device_id)
        ismanufactured = self.ispresent(DEVICES_TABLE, column, device_id)
        if ismanufactured:
            return isregistered     #returns T/F
        else:
            return not ismanufactured #returns false


    def update_subscription(self,subscription,device_id):
        self.cur.execute("UPDATE clients SET subscription_type=? WHERE device_id=?", (subscription,device_id))
        self.con.commit()
        return True

    def delete_one(self,table_name,column_name,data_id):
        self.cur.execute(f"DELETE FROM {table_name} WHERE {column_name}=?", (data_id,))
        self.con.commit()
        return True
        
    def delete_rows(self,table_name):
        self.cur.execute(f"DELETE FROM {table_name}")
        self.con.commit()
        return True
    