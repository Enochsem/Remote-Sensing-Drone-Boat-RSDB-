import sqlite3
import datetime
import time




class Database():
    DATABASE_NAME = "RSDB.db"
    USERS_TABLE = "users"
    DEVICES_TABLE = "devices"
    SENSOR_TABLE = "sensors"
    CLIENT_TABLE = "clients" #not used
    

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

            return True
        return False


    def signin(self,user_id,password):
        self.cursor.execute("SELECT * FROM users WHERE user_id=? AND password=?", (user_id,password))
        data = self.cursor.fetchall()
        if len(data) > 0:
            #user_type = data[0][1]
            print("signed in: ",data)
            return data, True
        return {"response":"Invalid Credencials"}, False


    def insert_readings(self,sensor_data): #old
        sensor = sensor_data
        #insert data from the sensors (one data at a time)
        self.cursor.execute(f"INSERT INTO {self.SENSOR_TABLE}('device_id','sensor_type','sensor_reading','datetime')VALUES(?,?,?,?)",
        (sensor.device_id, sensor.sensor_type,sensor.reading,current_datetime))
        self.connection.commit()
        return True
        
    
    def insert_all_sensor_readings(self,data):
        query = "INSERT INTO sensors(device_id,sensor_type,sensor_reading)VALUES(?,?,?)"
        self.cursor.executemany(query, data)
        self.connection.commit()
        # self.connection.close()
        return True
      
    
    def insert(self,table,message, device_id, status):
        #insert data 
        self.cursor.execute(f"INSERT INTO {table}('message','device_id','status')VALUES(?,?,?)",
        (message, device_id,status))
        self.connection.commit()
        # self.connection.close()
        return True

    

    def checkThreshold (self,json_data,device_id):
        threshold = {"Ph": 8,"Temperature" : 32,"TDS": 400,"Turbidity": 150 }
        for sensor_key, sensor_reading in json_data.items():
            for threshold_key, threshold_value in threshold.items():
                if threshold_key == sensor_key: 
                    self.highThreshold(sensor_reading, threshold_value,threshold_key,device_id)
                    self.lowThreshold(sensor_reading, threshold_value,threshold_key,device_id)

    def highThreshold(self,sensor_reading,threshold_value,threshold_key,device_id):
        if int(sensor_reading) > threshold_value:
            message= f"Threshold of {threshold_value} reach for {threshold_key}"
            status = self.insert("notification", message, device_id, "1")
            time.sleep(0.3)

    def lowThreshold(self,sensor_reading,threshold_value,threshold_key,device_id):
        if int(sensor_reading) < threshold_value:
            message= f"{threshold_key}is below the threshold at {threshold_value}"
            status = self.insert("notification", message, device_id, "1")
            time.sleep(0.3)




    def select(self,table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        data = self.cursor.fetchall()
        return data

    def select_where(self,table_name,column_name,data):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name}=?", (data,))
        data = self.cursor.fetchall()
        return data

    def select_where2(self,table_name,whereColumn1,whereData1,whereColumn2,whereData2):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {whereColumn1}=? AND {whereColumn2}=?", (whereData1,whereData2))
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
            return ismanufactured #returns false


    def update_subscription(self,subscription_type,device_id):
        self.cursor.execute("UPDATE clients SET subscription_type=? WHERE device_id=?", (subscription_type,device_id))
        self.connection.commit()
        return True

    def update(self, table_name, column_name, where_column, update_data,column_id):
        self.cursor.execute(f"UPDATE {table_name} SET {column_name}=? WHERE {where_column}=?", (update_data,column_id))
        self.connection.commit()
        return True

    def update_where2(self, table_name, setColumn_name, setUpdate_data, where_columnID1, wColumn_id1, where_columnID2, wColumn_id2):
        self.cursor.execute(f"UPDATE {table_name} SET {setColumn_name}=? WHERE {where_columnID1}=? AND {where_columnID2}=?", (setUpdate_data,wColumn_id1, wColumn_id2))
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
    
                