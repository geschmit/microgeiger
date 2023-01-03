# (c) 2022 geschmit

# All data is taken from:
# https://d3s5r33r268y59.cloudfront.net/datasheets/23976/2021-06-15-14-56-07/RadSens-1v3_datasheet_ENG.pdf 

class I2C_ADDR:
    """
    References addresses for the geiger module's I2C. 
    """

    # External
    Base = 0x66                 # Root I2C Address

    # Device
    Device_ID = 0x00            # Device ID[R, 8bit, Default: 0x7D]
    Device_FIRM = 0x01          # Firmware version[R, 8bit]
    Device_ADDR = 0x10          # I2C Address location[R/W, 8bit, Default: 0x66]
    Device_HVG = 0x11           # High-voltage generator toggle[R/W, 8bit, Default: 0x01]
    Device_LED = 0x14           # Not documented in source above. Toggles LED[R/W, 8bit, Default: 0x01]

    # Radiation
    Radi_DINTE = 0x03           # Dynamic(<123 s.) radiation intensity[R, 24bit]
    Radi_SINTE = 0x06           # Static(==500 s.) radiation intensity[R, 24bit]
    Radi_SENS = 0x12            # Value coeffecient for intensity calculation[R/W, 16bit, Default: 0x69]

    # Pulse
    Pulse = 0x09                # Number of pulses since this value was last read[16bit]
    pass


class Geiger:
    """
    Geiger counter class, for easy interfacing w/ radiation data.
    """
    from busio import I2C

    def __init__(self, i2c: I2C, devAddr: int=I2C_ADDR.Base) -> None:
        self.i2c = i2c
        self.id = self.getID()
        self.firmVer = self.getFirm()

        pass

    # Getters, 8bit
    def getID(self) -> int:
        """
        Fetches the device's ID.
        """
        while not self.i2c.try_lock():
            pass
        
        try:
            cData = bytearray(1)
            self.i2c.writeto_then_readfrom(I2C_ADDR.Base,bytes([I2C_ADDR.Device_ID]),cData)
        finally:
            self.i2c.unlock()
        
        # I'm assuming it's little-endian. I'll have to check the datasheet.
        return int.from_bytes(cData,"little") 

    def getFirm(self) -> int:
        """
        Fetches the device's firmware number.
        """
        while not self.i2c.try_lock():
            pass
        
        try:
            cData = bytearray(1)
            self.i2c.writeto_then_readfrom(I2C_ADDR.Base,bytes([I2C_ADDR.Device_FIRM]),cData)
        finally:
            self.i2c.unlock()
        
        return int.from_bytes(cData,"little") 

    def getI2C(self) -> int:
        """
        Fetches the device's I2C address value.
        """
        while not self.i2c.try_lock():
            pass
        
        try:
            cData = bytearray(1)
            self.i2c.writeto_then_readfrom(I2C_ADDR.Base,bytes([I2C_ADDR.Device_ADDR]),cData)
        finally:
            self.i2c.unlock()
        
        return int.from_bytes(cData,"little") 

    def getVoltCtrl(self) -> bool:
        """
        Checks if the voltage controller is enabled or not.
        """
        while not self.i2c.try_lock():
            pass
        
        try:
            cData = bytearray(1)
            self.i2c.writeto_then_readfrom(I2C_ADDR.Base,bytes([I2C_ADDR.Device_HVG]),cData)
        finally:
            self.i2c.unlock()
        
        return int.from_bytes(cData,"little") == 0x01 and True or False

    # Getters, 16bit
    def getPulse(self) -> int:
        """
        Fetches the amount of pulses/ticks recorded by the counter 
        since this function was last called. This value resets
        after being called.
        """
        while not self.i2c.try_lock():
            pass
        
        try:
            cData = bytearray(2)
            self.i2c.writeto_then_readfrom(I2C_ADDR.Base,bytes([I2C_ADDR.Pulse]),cData)
        finally:
            self.i2c.unlock()
        
        return int.from_bytes(cData,"little") 

    # Getters, 24bit
    # I'm not exactly sure how to deal with a 24bit datatype
    # conversion in Python. As of now, I'm sure a int will work.
    def getDynamicIntensity(self) -> int:
        """
        Fetches the dynamic intensity(<123 s.) of radiation from 
        the device. This is best used when detecting short-range
        radiation.
        """
        while not self.i2c.try_lock():
            pass
        
        try:
            cData = bytearray(3)
            self.i2c.writeto_then_readfrom(I2C_ADDR.Base,bytes([I2C_ADDR.Radi_DINTE]),cData)
        finally:
            self.i2c.unlock()
        
        return int.from_bytes(cData,"little") 

    def getStaticIntensity(self) -> int:
        """
        Fetches the static intensity(==500 s.) of radiation from 
        the device. This is best used when detecting long-range
        radiation.
        """
        while not self.i2c.try_lock():
            pass
        
        try:
            cData = bytearray(3)
            self.i2c.writeto_then_readfrom(I2C_ADDR.Base,bytes([I2C_ADDR.Radi_SINTE]),cData)
        finally:
            self.i2c.unlock()
        
        return int.from_bytes(cData,"little") 

    def getCoeffecient(self) -> int:
        """
        Fetches the coeffecient for calculating radiation
        intensity levels.
        """
        while not self.i2c.try_lock():
            pass
        
        try:
            cData = bytearray(3)
            self.i2c.writeto_then_readfrom(I2C_ADDR.Base,bytes([I2C_ADDR.Radi_SENS]),cData)
        finally:
            self.i2c.unlock()
        
        return int.from_bytes(cData,"little") 

    # Setters, 8bit

    # TODO: figure this trash out. I don't understand I2C to save my life.
    def setI2C(self) -> int:
        """
        Sets the device's I2C address location to 
        the number given. 
        
        # It's probally a good idea you don't touch this.
        """
        while not self.i2c.try_lock():
            pass
        
        try:
            cData = bytearray(1)
            # self.i2c.writeto()
        finally:
            self.i2c.unlock()
        
        # I'm assuming it's little-endian. I'll have to check the datasheet.
        return int.from_bytes(cData,"little") 
