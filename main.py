import tinytuya as tt
import time

tt.set_debug(True)


# Device configuration
d = tt.BulbDevice(dev_id="bfaaaab901d0da729a5apm", address="192.168.1.103", local_key="xz~+F~'?i|AyCr:i")
d2 = tt.BulbDevice(dev_id="bf82ec2aa975f8be95qpfl",address="192.168.1.114",local_key="g0mXkd`u>W4Q#g<b")
d.set_version(3.3)
d.set_socketPersistent(True)
d.set_mode('colour', nowait=True)

# Fetch and display initial status
try:
    data = d.status()
    print(f"Initial Status: {data}")
except Exception as e:
    print(f"Error fetching initial status: {e}")


print(test)













## -----ANNOYING EFFECTS -----
def DiscoTime():
    while True:
        try:
            d.turn_on(switch=20)
            d.set_colour(r=0, g=0, b=255, nowait=True)
            time.sleep(1)


            # Check status after turning on
            data = d.status()
            print(f"After start of loop: {data}")

            # Turn off the device (DPS key 20)
            d.set_colour(r=0, g=255, b=0)
            time.sleep(1)


            # Check status after turning off
            data = d.status()
            print(f"After end of loop: {data}")

        except Exception as e:
            print(f"Error in loop: {e}")
            break


def rainbow():
    rbow = {
        "red": [255, 0, 0],
        "orange": [255, 127, 0],
        "yellow": [255, 200, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255],
        "indigo": [46, 43, 95],
        "violet": [139, 0, 255],
        "pink": [255, 182, 193],
        "brown": [165, 42, 42],
        "gray": [169, 169, 169],
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "cyan": [0, 255, 255],
        "magenta": [255, 0, 255],
        "teal": [0, 128, 128],
        "lime": [0, 255, 0],
        "navy": [0, 0, 128],
        "beige": [245, 245, 220],
        "turquoise": [64, 224, 208],
        "silver": [192, 192, 192],
        "gold": [255, 215, 0],
        "peach": [255, 218, 185],
        "plum": [221, 160, 221],
        "coral": [255, 127, 80],
        "lavender": [230, 230, 250],
        "mint": [189, 252, 201],
        "rose": [255, 0, 127],
        "chartreuse": [223, 255, 0],
        "amber": [255, 191, 0],
        "ivory": [255, 255, 240],
        "sapphire": [15, 82, 186],
        "ruby": [224, 17, 95]
    }
    for color in rbow:
        [r, g, b] = rbow[color]
        d.set_colour(r, g, b, nowait=False)  # nowait = Go fast don't wait for response
        time.sleep(1)

