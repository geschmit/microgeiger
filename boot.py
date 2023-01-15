# (c) 2022 geschmit

print("Booting...")

from usb_cdc import disable
from storage import disable_usb_drive
from config import boot

if boot.enable_serial == False:
    print("Serial disable requested; you're a maniac, you know")
    disable()

if boot.enable_usb == False:
    print("USB disable requested")
    disable_usb_drive()