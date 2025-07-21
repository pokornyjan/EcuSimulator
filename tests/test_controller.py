import unittest

from ecu.controller import ECUController


class TestEcuController(unittest.TestCase):
    def setUp(self):
        self.ecu = ECUController()
    
    def test_cooling_fan_activation(self):
        out = self.ecu.update(101, 1000, False)
        self.assertEqual(out["cooling_fan"], "ON")
        
        out = self.ecu.update(99, 1000, False)
        self.assertEqual(out["cooling_fan"], "OFF")
        
    def test_throttle_cut_logic(self):
        out = self.ecu.update(90, 650, True)
        self.assertTrue(out["throttle_cut"])
        self.assertTrue(out["idle_warning"])

        out = self.ecu.update(90, 1200, False)
        self.assertFalse(out["throttle_cut"])