import random


class TemperatureSensor():
    def __init__(self, initial_temp=70):
        self.temp = initial_temp
    
    def read(self):
        self.temp += random.uniform(0.1, 0.5)
        if random.random() < 0.1:
            if self.temp > 70:
                self.temp -= random.uniform(0.5, 1.0)
        return round(self.temp, 2)