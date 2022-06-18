#pin numbering mode already set in Pin class (BCM)
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

import time
import requests as req



class DroneBoat:
    
    #sensor data values
    PH = None
    TDS = None
    TEMPERATURE = None
    TURBIDITY = None
    
    RAW_DATA = []
    
    BASE_URL = ""
    
    DELAY = 5
    
    
    def __init__(self):
        self.spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)  # create the spi bus
        self.chip_select = digitalio.DigitalInOut(board.D5) # create the cs (chip select)
        self.mcp = MCP.MCP3008(self.spi, self.chip_select)# create the mcp object
        self.CHANNELS = [MCP.PO, MCP.P1, MCP.P2, MCP.P3]
        
        
    def dataFormat1(self):
        return {"ph": self.ph_channel, "temp": self.temperature_channel, "tds": self.tds_channel, "turbidity":self.turbidity_channel}
    
    def dataFormat(self):
        return {"ph": self.PH, "temp": self.TEMPERATURE, "tds": self.TDS, "turbidity":self.TURBIDITY}
    
    
    def setData(self):
        data = self.dataFormat()
        for index in range(len(self.RAW_DATA)):
            data_form[index] = self.RAW_DATA[index]
        return data  #return sensor data in map format
    
    def postData(self):
        body = self.dataFormat() #final map data  TODO set to final data
        url = f"{BASE_URL}/sensor_readings"
        response = req.post(url,json = body)
        if response.status == 201:
            data = response.json()
            self.logdata(data)
        else:
            body["error"] = response
            self.logdata(body)
    
    def fetchRawData(self):
        for channel in self.CHANNELS:
            RAW_DATA.append(AnalogIn(self.mcp, channel).value())
    
    def calibrateData(self):
        #take data and call another class insatnce with sensor data caliboration
        #(eg: if analog data is within a specific range(423.1 and 43.0) set it to a sensor data unit "7.5ph"  )
        pass
    
    def logdata(self,log):
        with open("rsdblog.txt", "a") as file:
            file.write = log
        #may be in the future the log will be sent to the API
