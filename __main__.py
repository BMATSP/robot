import socket
import json
import RPi.GPIO as GPIO

from time import sleep
# sleep for a sec so the daemon doesn't get its panties in a wad
sleep(1)


def calc_duty_cycle(val):
    return val * 5 + 7.5

LMOTORPIN = 23  # BCM
RMOTORPON = 24  # BCM

GPIO.setmode(GPIO.BCM)
GPIO.setup(LMOTORPIN, GPIO.OUT)
GPIO.setup(RMOTORPON, GPIO.OUT)

# PWM range: [2.5, 12.5], with 7.5 in the middle
l_motor = GPIO.PWM(LMOTORPIN, 50)
r_motor = GPIO.PWM(RMOTORPON, 50)
l_motor.start(7.5)
l_motor.start(7.5)

PORT = 8081

while 1:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', PORT))
    server.listen(1)

    client, addr = server.accept()
    while 1:
        data = client.recv(1024)
        if not data:
            break

        left, right = map(calc_duty_cycle, map(float, json.loads(data.decode('utf-8'))))
        print(left, right)
        l_motor.ChangeDutyCycle(left)
        r_motor.ChangeDutyCycle(right)
