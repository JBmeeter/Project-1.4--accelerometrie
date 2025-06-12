from machine import Pin
import utime
import sys

# Setup pins for ultrasonic sensor
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

# Constants
k = 28  # Spring constant (placeholder)
m = 1.2  # Mass (placeholder)

# Function to measure distance in cm
def measure_distance():
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
    return distance

type(measure_distance)

# === Calibration phase: 5 readings over 1 second ===
measurements = []
print("Calibrating...")
for i in range(10):
    distance = round(measure_distance(), 1)
    measurements.append(distance)
    print(f"Measurement {i+1}: {distance:.2f} cm")
    utime.sleep_ms(200)  # 200 ms delay => 5 readings in 1 second

# Compute average as reference distance (d0)
d0 = round(sum(measurements) / len(measurements), 0)

print(f"Calibration complete. Reference distance (d0) = {d0:.2f} cm\n")

# Open log file on Pico's internal flash
logfile = open("data_accelerometer.csv", "w")

# Write CSV header
logfile.write("Distance (cm),Effective Distance (cm),Acceleration (m/s^2)\n")

# === Continuous measurement phase ===
while True:
    
    distance = round(measure_distance(),0)
    d_eff = round(d0 - distance, 0)
    acceleration = round((d_eff * k) / m, 0)  # Hooke's Law: F = kx → a = F/m = kx/m
    
        # Log to file
    logfile.write(f"{distance},{d_eff},{acceleration}\n")
    logfile.flush()  # Ensure it's saved immediately
    
    # Optional: Print to Shell as well
    print(f"{distance} cm, Δ: {d_eff} cm, a: {acceleration} m/s^2")                                        

    utime.sleep_ms(100)  # Maintain 5 readings per second
    
logfile.close()
sys.stdout = sys.__stdout__  # Restore normal output
print("Logging complete.")  


