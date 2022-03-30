import requests 

class SMS :
    def __init__(self):
        self.sender = "RSDB"
        self.url = "https://sms.arkesel.com/sms/api?action=send-sms"
        self.APIKEY = "OnhkSzhGTWVwaWtnUENlYWs="


    def send (self,recipient, message):
        payload = {
            'api_key': self.APIKEY, 
            'to': recipient, 
            'from':self.sender,
            'sms':message
            }
        response = requests.get(self.url, params = payload)
        if response.status_code == 200:
            data = response.json()
            print(data)
        return data

 


if __name__ == "__main__":
    # pass
    # sms = SMS("0554317909", "Me", "testing my contact")
    # test = sms.send()
    sms1 = SMS()
    test = sms1.send("0554317909", "deposite made Gh100")
    print(test)






