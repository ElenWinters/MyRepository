from turtle import *

def playerSquare(x, y, size, color_name):
    up()
    goto(x, y)
    down()
    color(color_name)
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()

