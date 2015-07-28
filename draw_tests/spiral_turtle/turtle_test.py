import turtle

turtle.Screen()
turtle.screensize(500,500)
turtle.speed(4)
# turt = turtle.Turtle() you don't actually need to instantiate this object but u can

turtle.forward(200) # moves forward 50 pixels
turtle.right(90) # rotates in degrees
turtle.forward(200) 
turtle.right(90) 
turtle.forward(200) 
turtle.right(90) 
turtle.forward(200) 
turtle.right(90) 

# basic spirograph! :) notice each time the start position is not changing - only its direction!!
turtle.pensize(2)
turtle.pencolor("blue")

def spiral (numCirc, radius):
	for i in range(numCirc):
		turtle.circle(radius) # draw a circle at center
		turtle.right(360/numCirc) # rotate x degrees

spiral(5, 100)

turtle.exitonclick()