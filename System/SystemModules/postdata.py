import requests

class Post():
    END_POINT = "/sensor_readings"
    URL = ""+self.END_POINT
    def __init__(self, data):
        self.data = data

    
    def post(self):
        # post all sensor data
        response  = requests.post(url=self.URL, json=self.data)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            # log error
            return response.status_code


    


    def tojson(self):
        pass


    def fromjson(self):
        pass