# from here http://cs.calvin.edu/courses/cs/106/labs/cs106lab7.html & https://docs.python.org/2/library/turtle.html

import turtle
import math

# setup
turtle.Screen()
turtle.screensize(500,500)
turtle.ht() # make turtle invisible
turtle.pensize(2)

while True:

	answer = raw_input("would you like to draw a spirograph? y/n ")

	if answer == "y":
		# get user input
		r = float(raw_input("what radius do you want for the moving circle? "))  # classic = x
		R = float(raw_input("what radius do you want for the overall circle? ")) # classic = x - 10
		p = float(raw_input("offset of pen from moving circle ")) # classic = x/2
		color = raw_input("what pen color do you want? (in terms of color string) ")

		t = 0.0
		turtle.penup()
		turtle.pencolor(color)
		turtle.fillcolor(color)

		turtle.goto(0,-300)
		turtle.write("parameters: %g, %g, %g" % (r, R, p), True, align="center", font=("Arial", 10, "normal"))

		while t < 50.0:
			#turtle.setposition(0,0) note this makes a spiky one!
			x =(R+r)*math.cos(t) + p*math.cos((R+r)*(t/r)) # sometimes these are - ???
			y =(R+r)*math.sin(t) + p*math.sin((R+r)*(t/r))
			# turtle.penup() # dashed line!!!
			turtle.setposition(x,y)
			turtle.pendown()
			turtle.goto(x, y)
			t += 0.1

	elif answer == "n":
		# exit turtle - persistent window
		#turtle.mainloop()
		break