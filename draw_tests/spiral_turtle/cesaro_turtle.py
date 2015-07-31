import turtle as t 

t.Screen()
t.screensize(600,600)
t.speed(10)

# most basic cesaro
# size = 50
# t.forward(size)
# t.right(80)
# t.forward(size)
# t.right(-160)
# t.forward(size)
# t.right(80)
# t.forward(size)

def cesaro(order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [80,-160,80,0]:
            # how does this say forward?
            cesaro(order-1, size/3) # the recursive call with incrementor
            t.right(angle)

# basic cesaro square - built up from the simplest case completely explicit!
# size = 50
# for i in range(0,4):
#     for angle in [80,-160,80,90]:
#         t.forward(size)
#         t.right(angle)

# wrong but neat:: this draws on top of itself!!!!
# def cesaroSq(order, size):
#     if order == 0:
#         t.forward(size)
#     else:
#        for i in range(0,4):
#             for angle in [80,-160,80,90]:
#                 cesaroSq(order-1, size/3)
#                 t.right(angle)

# closer - but the fractal isn't drawing on every single line?
def cesaroSq(order, size):
    if order == 0:
        t.forward(size)
    else:
        for i in range(0,4):
            cesaroSq(order-1, size/3)
            for angle in [80,-160,80,90]:
                t.forward(size/3)
                t.right(angle)


cesaroSq(3, 300)

t.mainloop()