#!/usr/bin/env python
#Draws a bouncing red pixel similar to the car in Nightrider
import unicornhat as UH
import time
UH.brightness(0.1)              # Unicorn Hat Base Brightness
rate = 0.03                     # Time between frames
rest = 0.06                     # How long to rest on edges
c1 = 255                        # Colour Value RED
c2 = 0                          # Colour Value GREEN
c3 = 0                          # Colour Value BLUE
while True:
        s=4
        for x in range(8):
                UH.set_pixel(x, s, c1, c2, c3)
                UH.show()
                time.sleep(rate)
                if x>=1:
                        UH.set_pixel(x-1, s, 0, 0, 0)
                        UH.show()
        time.sleep(rest)
        for y in xrange(7,-1,-1):
                UH.set_pixel(y, s, c1, c2, c3)
                UH.show()
                time.sleep(rate)
                if y<=6:
                        UH.set_pixel(y+1, s, 0, 0, 0)
                        UH.show()
        time.sleep(rest)
