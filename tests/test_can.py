import unittest

from ecu.can_interface import CANBusEmulator


class TestCANBusEmulator(unittest.TestCase):
    def test_message_structure(self):
        can = CANBusEmulator()
        can.send(0x123, {"temp": 100, "rpm": 1500, "fan": "ON"})
        self.assertEqual(len(can.tx_log), 1)
        msg = can.tx_log[0]
        self.assertIn("timestamp", msg)
        self.assertEqual(msg["id"], 0x123)
        self.assertIn("data", msg)
        self.assertEqual(msg["data"]["temp"], 100)