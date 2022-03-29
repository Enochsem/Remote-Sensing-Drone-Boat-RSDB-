import sqlite3

#creating database connection
DATABASE_NAME = "RSDB.db"
connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()


def create_sensor_table(device_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    sensor_table = f""" CREATE TABLE IF NOT EXISTS {device_id}
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    sensor_type TEXT NOT NULL, 
    sensor_reading TEXT NOT NULL, 
    datetime TIMESTAMP NOT NULL
    )"""
    try:
        cursor.execute(sensor_table)
        connection.commit()
    except connection.Error as e:
        print("SENSOR TABLE ERROR : ",e)
    finally:
        if connection:
            connection.close()
            

users_table = """CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_type TEXT NOT NULL,
user_id TEXT NOT NULL,
device_id TEXT NULL,
password TEXT NOT NULL,
subscription_type TEXT  NULL
)"""

#table not used for now
clients_table = """CREATE TABLE IF NOT EXISTS clients(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id TEXT NOT NULL,
device_id TEXT NOT NULL,
subscription_type TEXT  NULL
)"""

#all manufactured drone boats
devices_table = """CREATE TABLE IF NOT EXISTS devices(
id INTEGER PRIMARY KEY AUTOINCREMENT,
device_type TEXT NOT NULL, 
device_id TEXT NOT NULL
)"""


# all sensors used
sensors_table = """CREATE TABLE IF NOT EXISTS sensors(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
sensor_type TEXT NOT NULL
)"""


def createDB():
    try:
        cursor.execute(users_table)
        connection.commit()
        cursor.execute(clients_table)
        connection.commit()
        cursor.execute(devices_table)
        connection.commit()
        print("commited")
    except connection.Error as e:
        print("ERROR OCCURED: ",e)
    finally:
        if connection:
            print("compeleted")
            connection.close()


def default_data(data,query):
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("commited")
    except connection.Error as error:
        print("defalut data: ",error)
    finally:
        if connection:
            connection.close()

    
users = [("ADMIN","admin", "admin")]
devices = [("Version 1.0", "001"),("Version 2.0", "011"),("Version 3.0", "101")]
users_query = """ INSERT INTO users(user_type,user_id,password)VALUES(?,?,?)"""
devices_query= """ INSERT INTO devices(device_type,device_id)VALUES(?,?)"""


if __name__ == "__main__":
    createDB()
    #default_data(users, users_query)
    #default_data(devices, devices_query)