
from geiger import Geiger
from adafruit_bus_device.i2c_device import I2CDevice
from board import SDA, SCL, I2C

Geiger(
    i2c=I2CDevice(
        i2c=I2C(
            scl=SCL,
            sda=SDA
        )
    )
)