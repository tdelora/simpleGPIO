# simpleGPIO
Basic script to trigger a Raspberry Pi GPIO pin.

![simpleGPIO](https://github.com/user-attachments/assets/8e2e06c5-2fb8-4d0f-a8c5-d2627f00f278)

## Setup
- Clips are colored wires with alligator clips with a DuPont connector
  - Amazon: https://a.co/d/iVMrlcs
- Resitstor means resistors...
  - Amazon: https://a.co/d/1mahULF
- PWR: Red clip to pin 1 (3.3v) with 330 ohm resistor
- GRD: Black clip to pin 34 (gnd) with 1K ohm resistor
- SWC: Blue clip to pin 16SWC: Blue clip to pin 16

## Execution
After starting script:After starting script:
- Touch SWC to PWR to trigger HIGH
- Touch SWC to GRD to trigger LOW

## Notes:
- Using GPIO.PUD_DOWN in GPIO.setup should keep pin in low state when SWC is not touching PWR. I have seen the pin jump to high when SWC not connected to either PWR or GND.
