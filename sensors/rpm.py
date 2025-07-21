import random


class RPMSensor():
    def __init__(self):
        self.rpm = 800

    def read(self):
        change = random.choice([-200, -100, 0, 100, 300])
        self.rpm = max(500, self.rpm + change)
        return self.rpm