import RPi.GPIO as GPIO
import time

# Pin assignment (BCM numbering)
RED = 9
YELLOW = 8
GREEN = 7

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)

def blink_yellow(times):
    for _ in range(times):
        GPIO.output(YELLOW, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(YELLOW, GPIO.LOW)
        time.sleep(0.5)

def loop():
    while True:
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(15)
        GPIO.output(RED, GPIO.LOW)
        
        blink_yellow(5)
        
        GPIO.output(GREEN, GPIO.HIGH)
        time.sleep(20)
        GPIO.output(GREEN, GPIO.LOW)
        
        blink_yellow(5)

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
