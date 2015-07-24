from plotdevice import *

size(600, 600)
color(mode=RGB)
background(0,.75)
clear(all)

stroke(0,.5)
strokewidth(10)
pen(cap = ROUND)
fill(80, .5)

for x, y in grid(10,10, 100, 100):
    with bezier(50+x, 50+y) as path:
        for i in range(2):
            arcto(random(50,100)+x,random(50,100)+y, ccw=False)

export("test.png")
            



            

