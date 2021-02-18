# ADXL345 Python library for Raspberry Pi
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
#
# This is a Raspberry Pi Python implementation to help you get started with
# the Adafruit Triple Axis ADXL345 breakout board:
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

import smbus, os
from time import sleep

busNumber = int(os.getenv("I2C_BUS"))

bus = smbus.SMBus(busNumber)

        sleep(5)
