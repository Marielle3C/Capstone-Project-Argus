import time

def traffic_light_sequence():
    lights = [("Red", 5), ("Green", 10), ("Yellow", 2)]
    while True:
        for color, duration in lights:
            print(f"Light is {color}")
            time.sleep(duration)

if __name__ == "__main__":
    traffic_light_sequence()