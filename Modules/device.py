import time

class DeviceSensor():

    def __init__(self,device_id=None, sensor_type=None, sensor_reading=None):
        self.device_id = device_id
        self.sensor_type = sensor_type
        self.sensor_reading = sensor_reading


    def tojson(self,rows):
        json_data = []
        for row in range(len(rows)):
            json_data.append({self.device_id : rows[row][0],self.sensor_type: rows[row][1],self.sensor_reading : rows[row][2]})
        return json_data      


    def toTuple(self,data, device_id):
        return [(device_id,sensor_type,str(sensor_reading)) for sensor_type, sensor_reading in data.items()]    

    
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
            status = database.insert("notification", message, device_id, "1")
            time.sleep(0.3)

    def lowThreshold(self,sensor_reading,threshold_value,threshold_key,device_id):
        if int(sensor_reading) < threshold_value:
            message= f"{threshold_key}is below the threshold at {threshold_value}"
            status = database.insert("notification", message, device_id, "1")
            time.sleep(0.3)    

