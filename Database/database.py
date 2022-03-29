import sqlite3
import datetime




class Database():
    DATABASE_NAME = "RSDB.db"
    USERS_TABLE = "users"
    DEVICES_TABLE = "devices"
    CLIENT_TABLE = "clients"
    

    current_datetime = datetime.datetime.now()

    def __init__(self):
        self.connection = sqlite3.connect(self.DATABASE_NAME)
        self.cursor = self.connection.cursor()


    def signup(self,user):
        _user = user
        print("in signup", _user.device_id)
        isregistered = self.check_device_id(_user.device_id)    #check if device exist/ is registered
        print(isregistered)
        if not isregistered: #true if check returns false
            self.cursor.execute(f"INSERT INTO {self.USERS_TABLE}('user_type','user_id', 'device_id', 'password')VALUES(?,?,?,?)", 
            (_user.user_type, _user.user_id, _user.device_id, _user.password))
            self.connection.commit()
            #insert data into client db  #this is on hold

            #on signup create sensor table to collect sensor reading
            self.create_sensor_table(_user.device_id)
            return True
        return False


    def signin(self,user_id,password):
        self.cursor.execute("SELECT * FROM users WHERE user_id=? AND password=?", (user_id,password))
        data = self.cursor.fetchall()
        if len(data) > 0:
            #user_type = data[0][1]
            print("signed in: ",data)
            return data, True
        return False


    def insert_readings(self,sensor_data):
        sensor = sensor_data
        dynamic_table_name = sensor.device_id
        #insert data from the sensors
        self.cursor.execute(f"INSERT INTO {dynamic_table_name}('sensor','reading','datetime')VALUES(?,?,?)",
        (sensor.sensor_type,sensor.reading,current_datetime))
        self.connection.commit()
        return True
        

    def select(self,table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        data = self.cursor.fetchall()
        return data

    def select_where(self,table_name,column_name,data):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name}=?", (data,))
        data = self.cursor.fetchall()
        return data


    def ispresent(self,table_name,column_name,data):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name}=?", (data,))
        data = self.cursor.fetchall()
        return len(data) > 0


    def check_device_id(self, device_id):
        #check if manufacturer has device or a client has already registered with the device id
        column = "device_id"
        isregistered = self.ispresent(self.USERS_TABLE, column, device_id)
        print("ispresent call is registered?: ", isregistered)
        ismanufactured = self.ispresent(self.DEVICES_TABLE, column, device_id)
        print("ispresent call2 is manufactured?: ", ismanufactured)
        if ismanufactured:
            return isregistered     #returns T/F
        else:
            return not ismanufactured #returns false


    def update_subscription(self,subscription,device_id):
        self.cursor.execute("UPDATE clients SET subscription_type=? WHERE device_id=?", (subscription,device_id))
        self.connection.commit()
        return True

    def delete_one(self,table_name,column_name,data_id):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {column_name}=?", (data_id,))
        self.connection.commit()
        return True
        
    def delete_rows(self,table_name):
        self.cursor.execute(f"DELETE FROM {table_name}")
        self.connection.commit()
        return True
    

    def create_sensor_table(self,device_id):
        if device_id != "":
            sensor_table = f""" CREATE TABLE IF NOT EXISTS {device_id}
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            sensor_type TEXT NOT NULL, 
            sensor_reading TEXT NOT NULL, 
            datetime TIMESTAMP NOT NULL
            )"""
            try:
                self.cursor.execute(sensor_table)
                self.connection.commit()
            except self.connection.Error as e:
                print("SENSOR TABLE ERROR : ",e)
            finally:
                if self.connection:
                    self.connection.close()
                