import unittest

from sensors.brake import BrakePedalSensor
from sensors.rpm import RPMSensor
from sensors.temperature import TemperatureSensor


class TestSensors(unittest.TestCase):
    def test_temperature_range(self):
        sensor = TemperatureSensor()
        for _ in range(100):
            temp = sensor.read()
            self.assertGreaterEqual(temp, 70)
            self.assertLessEqual(temp, 110)
    
    def test_rpm_range(self):
        sensor = RPMSensor()
        for _ in range(100):
            rpm = sensor.read()
            self.assertGreaterEqual(rpm, 500)
            self.assertLessEqual(rpm, 5000)
    
    def test_brake_sensor(self):
        sensor = BrakePedalSensor()
        for _ in range(100):
            self.assertIn(sensor.read(), [True, False])
