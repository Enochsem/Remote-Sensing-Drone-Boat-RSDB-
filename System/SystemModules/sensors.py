class Sensor:

    #sensors READING VALUES
    # PH_VALUE = None
    # TDS_VALUE = None
    # TEMPERATURE_VALUE = None
    # TURBIDITY_VALUE = None

    PH = "Ph"
    TDS = "TDS"
    TEMPERATURE = "Temperature"
    TURBIDITY = "Turbidity"
    
    def __init__(self):
        self.PH_VALUE = None
        self.TEMPERATURE_VALUE = None
        self.TDS_VALUE = None
        self.TURBIDITY_VALUE = None

    def twoListToJson(self, keyList,listOfTuple):
        return [dict(zip(keyList, data)) for data in listOfTuple]
    
    def dataFormat(self):
        return {self.PH: self.PH_VALUE, self.TEMPERATURE: self.TEMPERATURE_VALUE, self.TDS: self.TDS_VALUE, self.TURBIDITY:self.TURBIDITY_VALUE}

    def getKey(self, data):
        return [key for key in data.keys()]
        
    def keyList(self):
        return[self.PH, self.TEMPERATURE, self.TDS, self.TURBIDITY] # returns string list of sensor names

    def setDataFormat(self, RAW_DATA):
        data = self.dataFormat()
        keys = self.keyList()
        for index in range(len(RAW_DATA)):
            data[keys[index]] = str(RAW_DATA[index])
        return data  #returns sensor data in map format
