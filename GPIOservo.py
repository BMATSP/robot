import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# time in between sweeps (seconds)
delayTime = 2

# PWM range: [2.5, 12.5], with 7.5 in the middle
pwm = GPIO.PWM(17, 50)
pwm.start(7.5)

while True:
    time.sleep(delayTime)
    print("all the way forward")
    pwm.ChangeDutyCycle(12.5)
    time.sleep(delayTime)
    print("All the way back")
    pwm.ChangeDutyCycle(2.5)
