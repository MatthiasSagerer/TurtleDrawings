import turtle
import tkinter
import shapes
import letters
import time

def reset(sec):
    time.sleep(sec)
    ralf.clear()
    ralf.penup()
    ralf.goto(0, 0)
    ralf.seth(0)
    ralf.pendown()

window = turtle.Screen()
window.setup(width=1.0, height=1.0, startx=None, starty=None)
ralf = turtle.Turtle()
ralf.speed(100)


'''
shapes.spiralTunnel(ralf, 42, 5, 10)
reset(3)
shapes.polygonSpiral(ralf, 4, 2, 175, 40)
reset(3)
shapes.polygonSpiral(ralf, 4, 2, 175, 12)
'''

size = 100
for i in range(2):
    letters.letterA(ralf, size)
    letters.letterB(ralf, size)
    letters.letterC(ralf, size)
    letters.letterD(ralf, size)
    letters.letterE(ralf, size)
    letters.letterF(ralf, size)
    letters.letterG(ralf, size)
    letters.letterH(ralf, size)
    letters.space(ralf, size)



tkinter.mainloop()