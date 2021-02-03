import turtle
import tkinter
import shapes
import letters
import time


def reset(turtle, sec):
    time.sleep(sec)
    turtle.clear()
    turtle.up()
    turtle.goto(0, 0)
    turtle.seth(0)
    turtle.down()


def resetAndGoTo(turtle, x, y):
    turtle.clear()
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.down()


window = turtle.Screen()
window.setup(width=1.0, height=1.0, startx=None, starty=None)
window.colormode(255)
ralf = turtle.Turtle()
ralf.speed(20)

resetAndGoTo(ralf, -300, 0)

letters.rainbowWrite(ralf, 150, 'Hello World')

reset(ralf, 3)

shapes.rainbowSpiralTunnel(ralf, 42, 5, 10)

reset(ralf, 3)

shapes.rainbowPolygonSpiral(ralf, 4, 2, 175, 40)

reset(ralf, 3)

shapes.rainbowPolygonSpiral(ralf, 4, 2, 175, 12)

tkinter.mainloop()
window.exitonclick()
