import math

def polygon(turtle, edges, sidelength):
    for i in range(edges):
       turtle.forward(sidelength)
       turtle.right(360/edges)

def polygonSpiral(turtle, edges, difference, iterations, deg):
    for i in range(iterations):
        polygon(turtle, edges, difference*i)
        turtle.right(deg)

def spiralTunnel(turtle, iteration, initialsize, deg):
    radDeg = deg*math.pi/180
    length = initialsize
    for i in range(iteration):
        if i != 0:
            turtle.left(deg)
            dist = length*math.sin(radDeg)
            turtle.backward(dist)
            length = length*(math.sin(radDeg)+math.cos(radDeg))
        polygon(turtle, 4, length)
