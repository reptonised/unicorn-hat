#!/usr/bin/env python
#
# Pulses an image of a blue skull on the unicorn hat 
# Looks best with the pibow modification layers diffuser
#
import unicornhat as UH
import time
UH.rotation(180)      # Sets the Orientation
UH.brightness(0.1)    # Overall Brightness
rate = 0.001          # Time between frames
rest = 3              # Time Between Pulses


while True:
        for t1 in range(510):
                t = t1/2
                # Row 1
                UH.set_pixel(2, 0, 0, t, t)
                UH.set_pixel(3, 0, 0, t, t)
                UH.set_pixel(4, 0, 0, t, t)
                UH.set_pixel(5, 0, 0, t, t)
                UH.set_pixel(6, 0, 0, t, t)
                # Row 2
                UH.set_pixel(1, 1, 0, t, t)
                UH.set_pixel(2, 1, 0, t, t)
                UH.set_pixel(3, 1, 0, t, t)
                UH.set_pixel(4, 1, 0, t, t)
                UH.set_pixel(5, 1, 0, t, t)
                UH.set_pixel(6, 1, 0, t, t)
                UH.set_pixel(7, 1, 0, t, t)
                # Row 3
                UH.set_pixel(0, 2, 0, t, t)
                UH.set_pixel(3, 2, 0, t, t)
                UH.set_pixel(6, 2, 0, t, t)
                UH.set_pixel(7, 2, 0, t, t)
                # Row 4
                UH.set_pixel(0, 3, 0, t, t)
                UH.set_pixel(1, 3, 0, 0, t)
                UH.set_pixel(3, 3, 0, t, t)
                UH.set_pixel(4, 3, 0, 0, t)
                UH.set_pixel(6, 3, 0, t, t)
                UH.set_pixel(7, 3, 0, t, t)
                # Row 5
                UH.set_pixel(0, 4, 1, 0, t)
                UH.set_pixel(1, 4, 0, t, t)
                UH.set_pixel(2, 4, 0, t, t)
                UH.set_pixel(4, 4, 0, t, t)
                UH.set_pixel(5, 4, 0, t, t)
                UH.set_pixel(6, 4, 1, 0, t)
                # Row 6
                UH.set_pixel(1, 5, 0, t, t)
                UH.set_pixel(2, 5, 0, t, t)
                UH.set_pixel(3, 5, 0, t, t)
                UH.set_pixel(4, 5, 0, t, t)
                UH.set_pixel(5, 5, 0, t, t)
                # Row 7
                UH.set_pixel(1, 6, 0, t, t)
                UH.set_pixel(2, 6, 1, 0, t)
                UH.set_pixel(3, 6, 0, t, t)
                UH.set_pixel(4, 6, 1, 0, t)
                UH.set_pixel(5, 6, 0, t, t)
                UH.show()
                time.sleep(rate)

        for t2a in range(510, -1, -1):
                t2 = t2a/2
                # Row 1
                UH.set_pixel(2, 0, 0, t2, t2)
                UH.set_pixel(3, 0, 0, t2, t2)
                UH.set_pixel(4, 0, 0, t2, t2)
                UH.set_pixel(5, 0, 0, t2, t2)
                UH.set_pixel(6, 0, 0, t2, t2)
                # Row 2
                UH.set_pixel(1, 1, 0, t2, t2)
                UH.set_pixel(2, 1, 0, t2, t2)
                UH.set_pixel(3, 1, 0, t2, t2)
                UH.set_pixel(4, 1, 0, t2, t2)
                UH.set_pixel(5, 1, 0, t2, t2)
                UH.set_pixel(6, 1, 0, t2, t2)
                UH.set_pixel(7, 1, 0, t2, t2)
                # Row 3
                UH.set_pixel(0, 2, 0, t2, t2)
                UH.set_pixel(3, 2, 0, t2, t2)
                UH.set_pixel(6, 2, 0, t2, t2)
                UH.set_pixel(7, 2, 0, t2, t2)
                # Row 4
                UH.set_pixel(0, 3, 0, t2, t2)
                UH.set_pixel(1, 3, 1, 1, t2)
                UH.set_pixel(3, 3, 0, t2, t2)
                UH.set_pixel(4, 3, 1, 1, t2)
                UH.set_pixel(6, 3, 0, t2, t2)
                UH.set_pixel(7, 3, 0, t2, t2)
                # Row 5
                UH.set_pixel(0, 4, 1, 1, t2)
                UH.set_pixel(1, 4, 0, t2, t2)
                UH.set_pixel(2, 4, 0, t2, t2)
                UH.set_pixel(4, 4, 0, t2, t2)
                UH.set_pixel(5, 4, 0, t2, t2)
                UH.set_pixel(6, 4, 1, 1, t2)
                # Row 6
                UH.set_pixel(1, 5, 0, t2, t2)
                UH.set_pixel(2, 5, 0, t2, t2)
                UH.set_pixel(3, 5, 0, t2, t2)
                UH.set_pixel(4, 5, 0, t2, t2)
                UH.set_pixel(5, 5, 0, t2, t2)
                # Row 7
                UH.set_pixel(1, 6, 0, t2, t2)
                UH.set_pixel(2, 6, 1, 1, t2)
                UH.set_pixel(3, 6, 0, t2, t2)
                UH.set_pixel(4, 6, 1, 1, t2)
                UH.set_pixel(5, 6, 0, t2, t2)
                UH.show()
                time.sleep(rate)
        time.sleep(rest)
