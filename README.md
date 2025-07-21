# 🧠 ECU Simulator

![Unit Tests](https://github.com/your-username/EcuSimulator/actions/workflows/unit_tests.yml/badge.svg)

An educational Engine Control Unit (ECU) simulator written in Python. This project emulates core ECU functionality such as sensor data reading, control logic processing, CAN message emulation, and logging — ideal for automotive software portfolio development and testing control logic without hardware.

---

## 🚗 Features

- Simulated real-time sensor data: temperature, RPM, brake pedal
- ECU control logic: cooling fan, throttle cut, idle warning
- CAN message emulation
- Output module for hardware abstraction
- JSON logging of all control decisions
- Basic visualization of ECU activity logs
- Unit-tested control and sensor modules
- GitHub Actions CI on PRs and manual trigger

---

## 🧰 Technologies

- Python 3.11
- `unittest` for testing
- GitHub Actions for CI
- JSON for log output
- Matplotlib for log visualization (optional)

---