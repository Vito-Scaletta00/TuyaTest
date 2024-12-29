import local_tuya as lt
import tinytuya as tt
import time

tt.set_debug(True)

d = tt.Device(dev_id="bf82ec2aa975f8be95qpfl", address="192.168.1.114", local_key="g0mXkd`u>W4Q#g<b")
d.set_dpsUsed({"1": None})
d.set_version(3.3)
d.set_socketPersistent(True)

# get initial status
data = d.status()
print(f"Initial Status: {data}")

while True:
    # Turn on the device
    d.turn_on()
    time.sleep(1)

    # Get updated status after turning on
    data = d.status()
    print(f"After Turn On: {data}")

    # Turn off the device
    d.turn_off()
    time.sleep(1)

    # Get updated status after turning off
    data = d.status()
    print(f"After Turn Off: {data}")