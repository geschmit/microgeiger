# (c) 2022 geschmit

# geiger module
from geiger import Geiger

# display
from displayio import FourWire
from adafruit_ili9341 import ILI9341

# neopixel
from neopixel import NeoPixel
from rainbowio import colorwheel

# multiple
from digitalio import DigitalInOut, Direction, Pull
from busio import SPI, I2C
from time import sleep
from board import (
    # Display SPI interface
    SCK,
    MOSI,
    MISO,

    # Additional display pins
    D10, # Command
    D9,  # CS
    D6,  # Reset

    # I2C interface
    SCL,
    SDA,

    # Leds
    RED_LED,
    BLUE_LED,
    NEOPIXEL
)

# Initialize the stuff
pix = NeoPixel(NEOPIXEL,1,brightness=0.3,auto_write=False)
bLed = DigitalInOut(BLUE_LED)
rLed = DigitalInOut(RED_LED)

bus = FourWire(
    SPI(clock=SCK,MOSI=MOSI,MISO=MISO), command=D10, chip_select=D9, reset=D6
)

disp = ILI9341(bus, width=320, height=240)
geig = Geiger(i2c=I2C(scl=SCL, sda=SDA))

# the stuff we work with
neoRgb = False # currently cycling neopixel rgb? (gaming geiger)

# the stuff we shouldn't change
vers = 1.0

print("HELLO- MicroGeiger")
print("(c) 2022 geschmit")
print("Funded by Hack Club!")
print("mGeig ver. %s", str(vers))
print("Awaiting geiger response...")
print("Geiger ver: %s", str(geig.firmVer))


# the engine belt
while True:
    pass