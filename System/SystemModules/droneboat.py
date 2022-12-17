#pin numbering mode already set in Pin class (BCM)
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

import time
from datetime import datetime as date
import requests as req

from sensors import Sensor
from calibrate import Calibrate
from postdata import Post
from ds8b20 import OneWireTemperature
import json


class DroneBoat:
    
    #sensor data values
    PH = None
    TDS = None
    TEMPERATURE = None
    TURBIDITY = None
    
    RAW_DATA = []
    
    BASE_URL = ""
    
    DELAY = 5
    
    sensor = Sensor()
    calibrate = Calibrate()
    post_data = Post()
    w1_temperature = OneWireTemperature()
    
    
    def __init__(self):
        self.spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)  # create the spi bus
        self.chip_select = digitalio.DigitalInOut(board.D8) # create the cs (chip select)
        self.mcp = MCP.MCP3008(self.spi, self.chip_select)# create the mcp object
        self.CHANNELS = [MCP.P4, MCP.P5, MCP.P6, MCP.P7]
        
    def dataFormat(self):
        return {"ph": self.PH, "temp": self.TEMPERATURE, "tds": self.TDS, "turbidity":self.TURBIDITY}
    
    
    #setData #return sensor data in map format
    
    
    def voltages(self):
        return self.RAW_DATA
    

    def readRawChannel(self,channel):
        return AnalogIn(self.mcp, self.CHANNELS[channel]).voltage
    
    def fetchRawData(self):
        for channel in self.CHANNELS:
            self.RAW_DATA.append(AnalogIn(self.mcp, channel).voltage)

    #{"PH" : [3,3], "TEMPERATURE" : [3,2],"TDS" : [3,1], "TURBIDITY" : [6,8]}
    def rawReading(self):
        counter = 0
        number_of_readings = 2
        dataDict = {"Ph": [], "Temperature":[], "TDS": [], "Turbidity":[]}
        for value in dataDict.values():
            for i in range(number_of_readings):
                channel = self.CHANNELS[counter]
                value.append(AnalogIn(self.mcp, channel).voltage)
                time.sleep(0.5)
            counter +=1
        return dataDict
    
    # average the readings
    def readingAverage(self):
        rawData = self.rawReading()
        values = []
        for data in rawData.values():
            values.append(sum(data)/len(data))
        return values
    
    def averageReading(self):
        return [sum(data)/len(data) for data in self.rawReading().values()]

    def calibratedData(self,data):
        #take data and call another class insatnce with sensor data caliboration
        #(eg: if analog data is within a specific range(423.1 and 43.0) set it to a sensor data unit "7.5ph"  )
        return self.calibrate.calibration(data)
    
    # //TODO remove post data from this module into its own
    #log post result with log_type specified
    def logPostResponse(self, postResponse):
        if isinstance(postResponse,int):
            self.logdata(postResponse, log_type="Post Error")
        elif postResponse["response"] == "Received" :
            self.logdata(postResponse["response"], log_type="Post Success")
        else:
            self.logdata(postResponse, log_type="Server Error")
    
    def logdata(self,log, log_type = "Sensor data"):
        data = f"{log_type} ==> {log} ==> {date.now()} \n"
        with open("rsdblog.txt", "a", encoding="utf8") as file:
            file.write(data)
        #may be in the future the log will be sent to the API
            
    def runDB(self):
        #raw_data = self.rawReading()
        averageRawSensorData = self.averageReading()
        setRawData = self.sensor.setDataFormat(averageRawSensorData)
        calibrated_data = self.calibratedData(setRawData)
        calibrated_data['Temperature'] = self.w1_temperature.celsiusTemperature()
        self.logdata(calibrated_data)
        post_response = self.post_data.post(calibrated_data)
        self.logPostResponse(post_response)
        
            
    
if __name__ == "__main__":
##    # while 1:
    #time.sleep(2)
    db = DroneBoat()
    #data = db.rawReading()
    #print(json.dumps(data,indent=4))
    avread = db.averageReading()
    print("average Readings",avread)
    setdata = db.sensor.setDataFormat(avread)
    print("setdata",setdata)
    clibratedData = db.calibratedData(setdata)
    clibratedData['Temperature'] = db.w1_temperature.celsiusTemperature()
    clibratedData['Ph'] =float(clibratedData['Ph'])/2
    clibratedData['Turbidity'] = round((float(clibratedData['Turbidity'])*-1)/10, 2)
    print("clibratedData",clibratedData)
    db.logdata(clibratedData)#log calibrated data
    post = db.post_data.post(clibratedData)
    print("post status",post)
    db.logPostResponse(post)
