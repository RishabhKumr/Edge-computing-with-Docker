import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import csv
TRIG = 23
ECHO = 24
print("Distance measurement in progresss")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print("Waiting for sensor to settle")
time.sleep(2)
def distcheck():
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)
    distance = round(distance,2)  
    return distance
f = open("/home/pi/Desktop/edge iot/test.csv","w",newline="")
rc=csv.writer(f)
rc.writerow(["Distance from sensor"])
for x in range(100):
    rc.writerow([distcheck()])
f.close()
