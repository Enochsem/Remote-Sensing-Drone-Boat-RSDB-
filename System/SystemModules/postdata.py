import requests
#from play import averageReading, setData

class Post():
    END_POINT = "sensor_readings"
    DEVICE_ID = "000"
    BASE_URL = "https://rsdbapi1.herokuapp.com"

    def __init__(self):
        self.url = f"{self.BASE_URL}/{self.END_POINT}/{self.DEVICE_ID}"

    
    def post(self, data):# post all sensor data
        response  = requests.post(url=self.url, json=data,)
        if response.status_code == 201:
            data = response.json()
            return data
        else:
            # log error
            return response.status_code


    


    def tojson(self):
        pass


    def fromjson(self):
        pass



if __name__ == "__main__":
    data = averageReading()
    body = setData(data)

    send = Post()
    response = send.post(body)
    print(response)
