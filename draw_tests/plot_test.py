#!/usr/bin/env python
# enoding: utf-8
import time
start = time.time()

from plotdevice import *

print "time to import: %g" % (time.time()-start)

size(600, 600)
color(mode=RGB, range=255)
background(0,75)


for x, y in grid(10,10,12,12):
    rect(x,y,10,10)

arc(50,50,50)

text("The Rest of San Francisco",140,430,fontsize=16,family="Hammersmith One")
text("Parking",392,190,fontsize=12,family="Hammersmith One")
export("/Users/karen/dev/drawBot/test.png")


