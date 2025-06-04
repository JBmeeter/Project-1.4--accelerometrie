from machine import Pin
import utime
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
k = 1
m = 1
d0 = 5

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   d_eff = d0 - distance
   acceleration = (distance*k/m)
   print("The distance from object is ",distance,"cm")
   print("The acceleration is", acceleration, "m/s^")

while True:
   ultra()
   utime.sleep(1)