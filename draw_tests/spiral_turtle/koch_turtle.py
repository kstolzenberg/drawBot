# http://openbookproject.net/thinkcs/python/english3e/recursion.html
import turtle as t

t.Screen()
t.screensize(512,512)
t.speed(10)

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
def kochSnow(order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [-120,60]:
            koch(order-1, size/3)
            t.left(angle)
            koch(order-1, size/3)
            t.left(angle)

kochSnow(3,400)

t.mainloop()
