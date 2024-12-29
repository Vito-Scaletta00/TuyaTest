import tinytuya as tt
import time

tt.set_debug(True)

# Device configuration
d = tt.Device(dev_id="bfaaaab901d0da729a5apm", address="192.168.1.103", local_key="xz~+F~'?i|AyCr:i")
d.set_version(3.3)
d.set_socketPersistent(True)

# Fetch and display initial status
try:
    data = d.status()
    print(f"Initial Status: {data}")
except Exception as e:
    print(f"Error fetching initial status: {e}")

while True:
    try:
        # Turn on the device (DPS key 20)
        d.set_status(True, 20)  # True for ON
        time.sleep(1)

        # Check status after turning on
        data = d.status()
        print(f"After Turn On: {data}")

        # Turn off the device (DPS key 20)
        d.set_status(False, 20)  # False for OFF
        time.sleep(1)

        # Check status after turning off
        data = d.status()
        print(f"After Turn Off: {data}")

    except Exception as e:
        print(f"Error in loop: {e}")
        break