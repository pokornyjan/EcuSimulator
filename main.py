import time

from ecu.can_interface import CANBusEmulator
from ecu.controller import ECUController
from outputs.actuators import CoolingFan, IdleWarningLight, ThrottleCut
from sensors.brake import BrakePedalSensor
from sensors.rpm import RPMSensor
from sensors.temperature import TemperatureSensor

temp_sensor = TemperatureSensor()
rpm_sensor = RPMSensor()
brake_sensor = BrakePedalSensor()

ecu_controller = ECUController()
can = CANBusEmulator()

fan = CoolingFan()
warning_light = IdleWarningLight()
throttle = ThrottleCut()

print("Starting ECU Simulation...")
try:
    for i in range(20):
        temp = temp_sensor.read()
        rpm = rpm_sensor.read()
        brake = brake_sensor.read()
    
        outputs = ecu_controller.update(temp, rpm, brake)
    
        fan.activate(outputs['cooling_fan'])
        warning_light.activate(outputs['idle_warning'])
        throttle.apply(outputs['throttle_cut'])
    
        can_data = {
            "temp": temp,
            "rpm": rpm,
            "brake": brake,
            "fan": outputs['cooling_fan'],
            "idle_warn": outputs['idle_warning'],
            "throttle_cut": outputs['throttle_cut']
        }
    
        can.send(message_id=0x123, data=can_data)
    
        print(f"[{i}] | Temp {temp} deg | RPM {rpm} | Brake: {'PRESSED' if brake else 'OFF'}")
        time.sleep(0.75)
except KeyboardInterrupt:
    print("Simulation interrupted")
finally:
    can.save_log()