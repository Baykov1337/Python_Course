class TemperatureConvertor:
    fahrenheit = "F"
    celsius = "C" 

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9*c/5 + 32
    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5* (f-32)/9
    
    @staticmethod
    def format(value, unit):
        if unit == TemperatureConvertor.fahrenheit: 
            return str(value) + str(unit)
        if unit == TemperatureConvertor.celsius:
            return str(value) + str(unit)
        
f = TemperatureConvertor.celsius_to_fahrenheit(35)
c = TemperatureConvertor.fahrenheit_to_celsius(100)
print (TemperatureConvertor.format(f,TemperatureConvertor.fahrenheit))
print (TemperatureConvertor.format(c,TemperatureConvertor.celsius))
        
