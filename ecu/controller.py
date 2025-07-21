class ECUController():
    def __init__(self):
        self.outputs = {
            "cooling_fan": "OFF",
            "idle_warning": False,
            "throttle_cut": False
        }
    
    def update(self, temperature, rpm, brake_pedal):
        if temperature > 95:
            self.outputs["cooling_fan"] = "ON"
        else:
            self.outputs["cooling_fan"] = "OFF"
        
        self.outputs["idle_warning"] = rpm < 600
    
        self.outputs["throttle_cut"] = brake_pedal
        
        return self.outputs