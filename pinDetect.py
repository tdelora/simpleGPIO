import RPi.GPIO as GPIO
import time

# Set pin numbering mode
GPIO.setmode(GPIO.BCM)

# This is a basic script to trigger a Raspberry Pi GPIO pin (16).

# Notes
# Clips mean colored wires with an alligator clip and a DuPont connector
#  - Amazon: https://a.co/d/iVMrlcs
# Resistor means resistors...
#  - Amazon: https://a.co/d/1mahULF
# PWR: Red clip to pin 1 (3.3v) with 330 ohm resistor
# GRD: Black clip to pin 34 (gnd) with 1K ohm resistor
# SWC: Blue clip to pin 16
#
# After starting the script:
#  - touch SWC to PWR to trigger HIGH
#  - Touch SWC to GRD to trigger LOW

# Define the GPIO pin you want to monitor
gpioPin = 16

# Set the pin, using GPIO.PUD_DOWN in GPIO.setup should keep the pin state low
# when SWC is not touching PWR.
GPIO.setup(gpioPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

try:
    while True:
        # Read the pin's state
        pin_state = GPIO.input(gpioPin)

        # Print the state
        if pin_state == GPIO.HIGH:
            print(f"Pin {gpioPin} is HIGH")
        else:
            print(f"Pin {gpioPin} is LOW")

        time.sleep(0.5) # Add a small delay to avoid flooding the output

except KeyboardInterrupt:
    GPIO.cleanup() # Clean up GPIO on script exit
