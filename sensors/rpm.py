import random


class RPMSensor():
    def __init__(self):
        self.rpm = 800

    def read(self):
        change = random.choice([-200, -100, 0, 100, 300])
        if self.rpm + change < 5000:
            self.rpm = max(500, self.rpm + change)
        return self.rpm