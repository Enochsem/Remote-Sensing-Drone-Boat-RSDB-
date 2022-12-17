
#{"PH" : [3,3,6,3], "TEMPERATURE" : [3,2,6,2],"TDS" : [3,1,6,1], "TURBIDITY" : [3,5,6,8]}

def listToJson(keyList,listOfTuple):
    return [dict(zip(keyList, data)) for data in listOfTuple]

keyList = ["PH", "TEMPERATURE","TDS", "TURBIDITY"]



CHANNELS = [1,2,3,4]
def rawReading():
    counter = 0
    number_of_readings = 2
    dataDict = {"ph": [], "temp":[], "tds": [], "turbidity":[]}
    for itemList in dataDict.values():
        for i in range(number_of_readings):
            itemList.append(CHANNELS[counter])
        counter +=1
    return dataDict
                   
# print("final",rawReading())



# average the readings
def readingAverage():
    rawData = rawReading()
    values = []
    for data in rawData.values():
        values.append(sum(data)/len(data))
    return values
# print("average readings", readingAverage())

def averageReading():
    return [sum(data)/len(data) for data in rawReading().values()]
# print("average readings2", averageReading())


#data format
def dataFormat():
    return {"Ph": None, "Temperature": None, "TDS": None, "Turbidity":None}
   
def setData(RAW_DATA): #TODO apply dict comprehension lateer
    data = dataFormat()
    key = ["Ph", "Temperature", "TDS", "Turbidity"]
    for index in range(len(RAW_DATA)):
        data[key[index]] = str(RAW_DATA[index])
    return data  #return sensor data in map format

data = readingAverage()
print("data format" ,setData(data))


#SENSOR CALIBRATION
def calibratePh(averageSensorData):
    cal = 21.34 - 0.07
    value = -5.70 * averageSensorData + cal
    return round(value, 2)

def calibrateTDS(averageVolt):
    temperature = 25
    compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0) #temperature compensation formula
    compensationVoltage = averageVolt / compensationCoefficient #temperature compensation
    tds_value = (133.42/compensationVoltage *compensationVoltage *compensationVoltage -255.86*compensationVoltage *compensationVoltage +857.39*compensationVoltage )*0.5 #constant for converting the volts to tds value ## don't really understand the constants yet #the last value apparently changes. in the TDS Sensor meter documentation, they used 1 
    tds_act = round(tds_value,2)

def calibrateTurbidity(averageReading):
    turbidty_value = -1120.4*(averageReading ** (1/2))+ 5742.3*averageReading-4352.9  #formula to convert the voltage to NTU
    return round(turbidty_value,2)
