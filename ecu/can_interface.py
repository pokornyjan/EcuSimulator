import json
import time
from pathlib import Path


class CANBusEmulator():
    def __init__(self, log_path="logs/can_log.json"):
        self.tx_log = []
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        
    
    def send(self, message_id: int, data: dict):
        timestamp = time.time()
        msg = {
            "timestamp": timestamp,
            "id": message_id,
            "data": data
        }
        self.tx_log.append(msg)
        self._print_can_message(msg)
    
    def _print_can_message(self, msg):
        print(f"[CAN Tx] ID: {hex(msg['id'])} | Data: {msg['data']} | Time: {msg['timestamp']}")
        
    def save_log(self):
        with open(self.log_path, "w") as f:
            json.dump(self.tx_log, f, indent=2)
        print(f"Log saved to: {self.log_path.resolve()}")