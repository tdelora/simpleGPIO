# simpleGPIO
Basic script to trigger a Raspberry Pi GPIO pin.

![simpleGPIO](https://github.com/user-attachments/assets/8e2e06c5-2fb8-4d0f-a8c5-d2627f00f278)

[audioGPIOTrigger](https://github.com/tdelora/audioGPIOTrigger/tree/main) is an extension of this project.

## Setup
- Clips are colored wires with an alligator clip and a DuPont connector
  - Amazon: https://a.co/d/iVMrlcs
- Resistor means resistor...
  - Amazon: https://a.co/d/1mahULF
- PWR: Red clip to pin 1 (3.3v) with 330 ohm resistor
- GRD: Black clip to pin 34 (gnd) with 1K ohm resistor
- SWC: Blue clip to pin 16

## Execution
After starting the script:
- Touch SWC to the resistor on PWR to trigger HIGH
- Touch SWC to the resistor on GRD to trigger LOW

## Notes:
- Using GPIO.PUD_DOWN in GPIO.setup should keep pin in low state when SWC is not touching PWR. I have seen the pin jump to high when SWC not connected to either PWR or GND.

## Applications
### Detecting when a phone is off the hook

![IMG_8785_princess](https://github.com/user-attachments/assets/225b8060-4fc1-4ff3-80fa-fedf3d4e5d05)

In this example, the PWR and SWC clips have been attached to a Bell System 702BM (Princess) dial telephone, connected to the wires that turn on the night light when the handset is off the hook. From the phone, the blue wire has been disconnected from terminal 4 and connected to the PWR clip resistor using a red wire with two alligator clips; the orange wire has been disconnected from terminal 2 and connected to the SWC clip directly. Take the handset off the hook to trigger HIGH, and place the handset on the hook to trigger LOW. The GND clip is not utilized in this setup.

Snapshot from the wiring diagram of a Bell System 702BM (Princess) phone showing the utilized orange and blue wires.

<img width="266" alt="Screenshot 2025-07-07 at 16 40 40" src="https://github.com/user-attachments/assets/0b23ea7a-bc5f-4ca7-9dd5-206a7656238c" />

