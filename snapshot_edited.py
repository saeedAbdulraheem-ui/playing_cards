# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Snapshot Example
#
# Note: You will need an SD card to run this example.
# You can use your OpenMV Cam to save image files.

import sensor
import time
import machine
import os

label = "spades" #set up label
extension = ".jpg" #use extension of jpg



sensor.reset()  # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)  # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)  # Set frame size to QVGA (320x240)
sensor.set_windowing(224, 224) #take photos of size 224 x 224

sensor.skip_frames(time=2000)  # Wait for settings take effect.

led = machine.LED("LED_BLUE")

start = time.ticks_ms()
while time.ticks_diff(time.ticks_ms(), start) < 4000:
    sensor.snapshot()
    led.toggle()

led.off()


count = 1 #start count at one

#check if the file name is present in the directory
while f"{label}.{count}{extension}" in os.listdir():
    count += 1 #increement the count by 1


filename = f"{label}.{count}{extension}" #setting up file name


img = sensor.snapshot() #take snapsnot
img.save(filename) #save file

raise (Exception("Please reset the camera to see the new file."))
