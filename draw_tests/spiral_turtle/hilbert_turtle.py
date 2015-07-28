# PASCAL to python Hilbert Fractal!!!
# := is assignment! ; separates statements!
# where h is line segment size

import turtle
import math
import random

turtle.Screen()
turtle.screensize(512,512)

n = 4 # depth counter
h0 = 512

def A (h):
	turtle.backward(h)
	turtle.left(-90)
	turtle.forward(h)
	turtle.right(90)
	turtle.backward(h)

def B (h):
	turtle.left(90)
	turtle.forward(h)
	turtle.right(90)
	turtle.forward(h)
	turtle.right(90)
	turtle.forward(h)

def C (h):
	turtle.forward(h)
	turtle.left(90)
	turtle.forward(h)
	turtle.left(90)
	turtle.forward(h)

def D (h):
	turtle.right(90)
	turtle.forward(h)
	turtle.right(90)
	turtle.forward(h)
	turtle.right(90)
	turtle.forward(h)

# need to recursively define each step in terms of each other? how will this work?
# i wonder if you could also do this with setheading?

#A(100)
#B(100)
#C(100)
#D(100)

# temp hack
allFunctions = [A, B, C, D]
draw_length = int(raw_input("how many loops to draw for? "))

# for x turns, randomly pick which function to draw
for i in range(draw_length):
	random.choice(allFunctions)(150)

turtle.mainloop() 