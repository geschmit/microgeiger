# BECAUSE ADAFRUIT DOESNT HAVE CONFIGPARSER APPARENTLY

"""
[geiger]
unit = "cpm"            # Unit displayed, either in CPM, Rads or Sievert.
enable_ticks = True     # Enables the geiger ticking when a pulse is detected.

[boot]
enable_usb = True       # Enables the USB storage.
enable_bt = True        # Enables the Bluetooth UART console. 
enable_serial = True    # Enables the serial console. It's good you don't touch this.

[sys]
version = 1.0           # Version of the code.
"""

class geiger:
    unit = "cpm"            # Unit displayed, either in CPM, Rads or Sievert.
    enable_ticks = True     # Enables the geiger ticking when a pulse is detected.
    pass

class boot:
    enable_usb = True       # Enables the USB storage.
    enable_bt = True        # Enables the Bluetooth UART console. 
    enable_serial = True    # Enables the serial console. It's good you don't touch this.
    pass

class sys:
    version = 1.0           # Version of the code.
    pass
