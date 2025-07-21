import random


class BrakePedalSensor():
    def read(self):
        return random.random() < 0.2