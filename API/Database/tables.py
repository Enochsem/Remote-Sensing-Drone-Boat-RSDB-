import sqlite3

#creating database connection
DATABASE_NAME = "RSDB.db"
connection = sqlite3.connect(DATABASE_NAME)

device_id = ""

sensor_table = f""" CREATE TABLE IF NOT EXISTS {device_id}(
                    id INTEGER PRINMARY KEY AUTOINCREAMENT,
                    sensor TEXT NOT NULL,
                    reading TEXT NOT NULL,
                    datetime TIMESTAMP NOT NULL
                    )"""


users_table = """CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRINMARY KEY AUTOINCREAMENT,
                    user_type TEXT NOT NULL,
                    user_id TEXT NOT NULL,
                    device_id TEXT NULL,
                    password TEXT NOT NULL
                    )"""


clients_table = """CREATE TABLE IF NOT EXISTS clients(
                    id INTEGER PRINMARY KEY AUTOINCREAMENT,
                    name TEXT NOT NULL,
                    device_id TEXT NULL,
                    subscription_type TEXT NOT NULL
                    )"""


devices_table = """CREATE TABLE IF NOT EXISTS devices(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Type TEXT NOT NULL, 
        device_id TEXT NOT NULL
        )"""