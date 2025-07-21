import unittest

from ecu.controller import ECUController


class TestEcuController(unittest.TestCase):
    def setUp(self):
        self.ecu = ECUController()
    
    def test_cooling_fan_activation(self):
        out = self.ecu.update({"temp": 101, "rpm": 1000, "brake": False})
        self.assertEqual(out["cooling_fan"], "ON")
        
        out = self.ecu.update({"temp": 99, "rpm": 1000, "brake": False})
        self.assertEqual(out["cooling_fan"], "OFF")
        
    def test_throttle_cut_logic(self):
        out = self.ecu.update({"temp": 90, "rpm": 650, "brake": True})
        self.assertTrue(out["throttle_cut"])
        self.assertTrue(out["idle_warning"])

        out = self.ecu.update(temp=90, rpm=1200, brake=False)
        self.assertFalse(out["throttle_cut"])