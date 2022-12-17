

class Calibrate:

    def __init__(self):
        pass

    def calibratePh(self,averageSensorData):
        cal = 21.34 - 0.07
        value = -5.70 * float(averageSensorData) + cal
        return round(value, 2)

    def calibrateTDS(self, averageVolt, temperature = 25.0):
        averageVolt = float(averageVolt)
        temperature = float(temperature)
        compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0) #temperature compensation formula
        compensationVoltage = averageVolt / compensationCoefficient #temperature compensation
        tds_value = (133.42/compensationVoltage *compensationVoltage *compensationVoltage -255.86*compensationVoltage *compensationVoltage +857.39*compensationVoltage )*0.5 #constant for converting the volts to tds value ## don't really understand the constants yet #the last value apparently changes. in the TDS Sensor meter documentation, they used 1 
        tds_act = round(tds_value,2)
        return str(tds_act)
    
    def calibrateTemperature(self, averageVoltage):
        return str(round(float(averageVoltage),2))

    def calibrateTurbidity(self, averageReading):
        turbidty_value =0
        averageReading = float(averageReading)
        if averageReading < 2.5:
            turbidty_value = 3000
        else:
            turbidty_value = -1120.4*(averageReading ** (1/2))+ 5742.3*averageReading-4352.9  #formula to convert the voltage to NTU
        return str(round(turbidty_value,2))

    def calibration(self,data):
        for key, value in data.items():
            if key == "Ph":
                data[key] = self.calibratePh(value)
            elif key == "Temperature":
                data[key] = self.calibrateTemperature(value)
            elif key == "TDS":
                temp = data["Temperature"]
                data[key] = self.calibrateTDS(value, temperature=temp)
            elif key == "Turbidity":
                data[key] = self.calibrateTurbidity(value)
        return data