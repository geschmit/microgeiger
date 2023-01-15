# (c) 2022 geschmit

# geiger module
from geiger import Geiger

# display
from displayio import FourWire
from adafruit_st7789 import ST7789

# neopixel
from neopixel import NeoPixel
from rainbowio import colorwheel

# multiple
from digitalio import DigitalInOut, Direction, Pull
from busio import SPI, I2C
from time import sleep
from configparser import ConfigParser
from board import (
    # Display SPI interface
    SCK,
    MOSI,
    MISO,

    # Additional display pins
    D9,   # SDCS
    D10,  # DC/Command
    D11,  # RESET
    D12,  # TCS/Chip select

    # I2C interface
    SCL,
    SDA,

    # Leds
    RED_LED,
    BLUE_LED,
    NEOPIXEL
)

# LEDs and display
pix = NeoPixel(NEOPIXEL,1,brightness=1,auto_write=False)
bLed = DigitalInOut(BLUE_LED)
rLed = DigitalInOut(RED_LED)

bus = FourWire(
    SPI(clock=SCK,MOSI=MOSI,MISO=MISO), command=D10, chip_select=D12, reset=D11,
)

disp = ST7789(bus, width=320, height=170)

# set this up last cuz it'll prob take the longest
geig = Geiger(i2c=I2C(scl=SCL, sda=SDA))

print("HELLO- MicroGeiger")
print("(c) 2022 geschmit")
print("Funded by Hack Club!")

# configurations
conf = ConfigParser() # ze config
conf.read("config.ini")

bt_cons = None
bt_buff = []
if conf.getboolean("sys","enable_bt") == True:
    from adafruit_ble import BLERadio
    from adafruit_ble.advertising.standard import ProvideServicesAdvertisement  
    from adafruit_ble.services.nordic import UARTService    
    bt_radio = BLERadio()
    bt_cons = UARTService()
    ProvideServicesAdvertisement(bt_cons)
    print("Bluetooth UART online...")

# the engine belt
while True:
    if bt_cons is None:
        pass
    else:
        if bt_cons.in_waiting > 0:
            while bt_cons.in_waiting > 0:
                readByte = bt_cons.read(1)
                if str(readByte) == "\n":
                    # cmd parse func here
                    # doCmd(str(bt_buff))
                    bt_buff.append("\n")
                    bt_cons.write(bt_buff)
                    bt_cons.reset_input_buffer()
                    bt_buff = []
                else:
                    bt_buff.append(readByte)
    