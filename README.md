# MicroGeiger: Damn small radiation dosimeter
This is my writeup on how to make a really compact geiger counter running CircuitPython.

This project was funded by the Hack Club "[Winter hardware wonderland](https://hackclub.com/winter)" project, which provided me with the funding to afford the hardware used.

# Hardware
TODO

# Usage
Commands can be inputted via UART console after connecting to the nRF board on the geiger.
| Category | Name | Desc |
| --- | --- | --- |
| System | `reboot` | Reboots geiger. |

# Disclaimer
- The SBM-20 tube is known to break when exposed to large amounts of radiation.
- The measurements in this aren't 100% accurate and more or less are just used to estimate how much radiation is around you.
