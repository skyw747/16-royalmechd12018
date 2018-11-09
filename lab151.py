from gpiozero import DistanceSensor
from time import sleep

sensor=DistanceSensor(echo=18 , trigger =17)
while True:
    print('Distance: ', sensor.distance * 100 ,'cm')
    sleep(1)
