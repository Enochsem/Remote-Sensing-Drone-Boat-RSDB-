

class DeviceSensor():

    def __init__(self,device_id, sensor_type, sensor_reading):
        self.device_id = device_id
        self.sensor_type = sensor_type
        self.sensor_reading = sensor_reading


    def tojson(self,rows):
        json_data = []
        for row in range(len(rows)):
            json_data.append({self.device_id : rows[row][0],self.sensor_type: rows[row][1],self.sensor_reading : rows[row][2]})
        return json_data            