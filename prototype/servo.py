from gpiozero import *

s = Servo(14, 0, 0.00070, 0.00255)

while True:
        s.value = float(input("Enter Value: "))