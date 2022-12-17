from w1thermsensor import W1ThermSensor, Unit

#temperature_in_all_units = sensor.get_temperatures([
#    Unit.DEGREES_C,
#    Unit.DEGREES_F,
#    Unit.KELVIN])


class OneWireTemperature:
    
    def __init__(self):
        self.ds18b20Sensor = W1ThermSensor()
    
    def celsiusTemperature(self):
        temperature = self.ds18b20Sensor.get_temperature()
        return str(round(temperature,2))
    
    def fahrenheitTemperature(self):
        temperature = self.ds18b20Sensor.get_temperature(Unit.DEGREES_F)
        return str(round(temperature,2))
    


if __name__ == "__main__":
    sensor = OneWireTemperature()
    tempc = sensor.celsiusTemperature()
    tempf = sensor.fahrenheitTemperature()
    print("tc",tempc,"tf",tempf)
    
