class CoolingFan():
    def __init__(self):
        self.state = "OFF"
    
    def activate(self, command):
        self.state = command
        print(f"Cooling Fan {self.state}")
    
class IdleWarningLight():
    def __init__(self):
        self.active = False
    
    def activate(self, warning_state):
        self.active = warning_state
        if warning_state:
            print("Idle warning light: ON")
        else:
            print("Idle warning light: OFF")
        

class ThrottleCut():
    def __init__(self):
        self.enabled = False
    
    def apply(self, should_cut):
        self.enabled = should_cut
        if should_cut:
            print("Throttle CUT (braking)")
        else:
            print("Throttle normal")