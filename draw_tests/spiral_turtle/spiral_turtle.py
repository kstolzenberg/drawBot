# from here http://cs.calvin.edu/courses/cs/106/labs/cs106lab7.html
import turtle
import math

# setup
turtle.Screen()
turtle.screensize(500,500)
turt = turtle.Turtle()

# get user input
r = raw_input("what radius do you want for the moving circle? ")
R = raw_input("what radius do you want for the overall circle? ")
p = raw_input("offset of pen from moving circle ")
color = raw_input("what pen color do you want? (in terms of color string) ")

t = 0.0
turtle.setposition(250,250)

while t < 100.0:
	turtle.penup()
	x =(R+r)math.cos(t) + p*math.cos((R+r)t/r)
	y =(R+r)math.sin(t) + p*math.sin((R+r)t/r)
	turtle.pencolor(color)
	turtle.pendown()
	turtle.goto(x, y)
	t += 0.1


# exit turtle - persistent window
turtle.mainloop()