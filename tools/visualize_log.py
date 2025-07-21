import json
from pathlib import Path

import matplotlib.pyplot as plt


def load_log(path="logs/can_log.json"):
    with open(path, "r") as f:
        return json.load(f)

def plot_signals(log_data):
    timestamps = [msg["timestamp"] - log_data[0]["timestamp"] for msg in log_data]
    temp = [msg["data"]["temp"] for msg in log_data]
    rpm = [msg["data"]["rpm"] for msg in log_data]
    brake = [1 if msg["data"]["brake"] else 0 for msg in log_data]
    throttle_cut = [1 if msg["data"]["throttle_cut"] else 0 for msg in log_data]
    fan_state = [1 if msg["data"]["fan"] == "ON" else 0 for msg in log_data]

    fig, axs = plt.subplots(4, 1, figsize=(12, 10), sharex=True)

    axs[0].plot(timestamps, temp, label="Engine Temp (°C)", color="orange")
    axs[0].set_ylabel("Temp")
    axs[0].legend()

    axs[1].plot(timestamps, rpm, label="RPM", color="blue")
    axs[1].set_ylabel("RPM")
    axs[1].legend()

    axs[2].step(timestamps, brake, label="Brake Pressed", where='post', color="red")
    axs[2].step(timestamps, throttle_cut, label="Throttle Cut", where='post', color="purple")
    axs[2].set_ylabel("Binary")
    axs[2].legend()

    axs[3].step(timestamps, fan_state, label="Cooling Fan ON", where='post', color="green")
    axs[3].set_ylabel("Fan")
    axs[3].set_xlabel("Time (s)")
    axs[3].legend()

    plt.tight_layout()
    plt.savefig("ecu_graph.png")
    plt.show()

if __name__ == "__main__":
    log_path = Path("logs/can_log.json")
    if not log_path.exists():
        print(f"Log file not found: {log_path}")
    else:
        data = load_log(log_path)
        plot_signals(data)