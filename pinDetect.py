import RPi.GPIO as GPIO
import signal, time

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
#  - touch SWC to resistor on PWR to trigger HIGH
#  - Touch SWC to resistor on GRD to trigger LOW

# Define the GPIO pin you want to monitor
gpioPin = 16

# Set the pin, using GPIO.PUD_DOWN in GPIO.setup should keep the pin state low
# when SWC is not touching PWR.
GPIO.setup(gpioPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try: 

  #
  # Function pinEventCallback is called when GPIO.add_event_detect (below)
  # detects an event on gpioPin.
  #

  def pinEventCallback(channel):
      if GPIO.input(channel):
          print(f"Pin {gpioPin} is HIGH")
      else:
          print(f"Pin {gpioPin} is LOW")

  # Read gpioPin's initial state at startup
  pin_state = GPIO.input(gpioPin)
  if pin_state == GPIO.HIGH:
    print(f"Pin {gpioPin} initial state is HIGH")
  else:
    print(f"Pin {gpioPin} initial state is LOW")

  # Add event detection for gpioPin for subsequent gpioPin state changes.
  GPIO.add_event_detect(gpioPin, GPIO.BOTH, callback=pinEventCallback, bouncetime=200)

  print(f"Ready for events on GPIO pin {gpioPin}.")

  # Use signal.pause() to keep from exiting until signaled.
  signal.pause()

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
