# http://openbookproject.net/thinkcs/python/english3e/recursion.html
import turtle as t

t.Screen()
t.screensize(800,800)
t.speed(10)
t.ht()
t.pensize(2)


# most basic koch:
# size = 40
# t.forward(size)
# t.left(60)
# t.forward(size)
# t.left(-120)
# t.forward(size)
# t.left(60)
# t.forward(size)

def koch(order, size):
    # rewrite with loop
    if order == 0:
        t.forward(size)
    else:
        for angle in [60,-120,60,0]:
            koch(order-1, size/3)
            t.left(angle)

# how to modify to get to a snowflake? this isn't there ...
# this gets half way around?!?!?![-120,60]
# when you call both - it goes too far!
def kochSnow(order, size):
    if order == 0:
        t.forward(size)
    else:
        angle_range = [-120,60,0,60,-120,60]

        for angle in angle_range:
            kochSnow(order-1, size/3) # hold up you were calling the original func!
            t.left(angle)
        return angle_range


angles = kochSnow(3,400)
t.penup()
t.goto(0,50)
t.write("angles: %s" % list(angles), True, align="center", font=("Arial", 10, "normal"))

t.mainloop()
