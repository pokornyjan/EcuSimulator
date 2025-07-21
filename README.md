# ECU Simulator

Engine Control Unit (ECU) simulator written in Python. This project emulates on simple examples core ECU functionality such as sensor data reading, control logic processing, CAN message emulation, and logging.

---

## Features

- Simulated real-time sensor data: temperature, RPM, brake pedal
- ECU control logic: cooling fan, throttle cut, idle warning
- CAN message emulation
- Output module for hardware abstraction
- JSON logging of all control decisions
- Basic visualization of ECU activity logs
- Unit-tested control and sensor modules
- GitHub Actions CI on PRs and manual trigger

---

## Technologies

- Python 3.11
- `unittest` for testing
- GitHub Actions for CI
- JSON for log output
- Matplotlib for log visualization (optional)

---
