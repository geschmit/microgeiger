# (c) 2022 geschmit

from geiger import Geiger
from board import I2C, SPI

geig = Geiger(i2c=I2C())
print("Geiger firm ver: %s", str(geig.firmVer))