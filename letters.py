import math


def space(turtle, size):
    turtle.up()
    turtle.forward(size/5)
    turtle.down()

def letterA(turtle, size):
    turtle.left(75)
    dist = size/math.cos(math.radians(15))
    turtle.forward(dist)
    turtle.right(150)
    turtle.forward(dist/2)
    turtle.right(105)
    dist2 = size*math.tan(math.radians(15))
    turtle.forward(dist2)
    turtle.up()
    turtle.backward(dist2)
    turtle.down()
    turtle.left(105)
    turtle.forward(dist/2)
    turtle.left(75)
    turtle.up()
    turtle.forward(size/20)
    turtle.down()

def letterB(turtle, size):
    dist = size/5
    dist2 = size/4
    turtle.forward(dist)
    turtle.circle(dist2, 180)
    turtle.forward(dist)
    turtle.right(180)
    turtle.forward(dist)
    turtle.circle(dist2, 180)
    turtle.forward(dist)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(dist)
    turtle.up()
    turtle.forward(dist2+dist/4)
    turtle.down()

def letterC(turtle, size):
    dist = size/4
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.right(180)
    turtle.circle(dist, 180)
    turtle.up()
    turtle.forward(size/2)
    turtle.down()
    turtle.circle(dist, 180)
    turtle.forward(dist*2)
    turtle.up()
    turtle.forward(dist)
    turtle.left(90)
    turtle.forward(dist*2.2)
    turtle.down()

def letterD(turtle, size):
    dist = size/2
    dist2 = size*3/40
    turtle.forward(dist2)
    turtle.circle(dist, 180)
    turtle.forward(dist2)
    turtle.left(90)
    turtle.forward(size)
    turtle.up()
    turtle.left(90)
    turtle.forward(dist*1.2)
    turtle.down()

def letterE(turtle, size):
    dist = size/2
    dist2 = size*7/16
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(dist2)
    turtle.right(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.right(90)
    turtle.forward(dist2)
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.left(90)
    turtle.forward(dist2)
    turtle.up()
    turtle.forward(dist/10)
    turtle.down()

def letterF(turtle, size):
    dist = size/2
    dist2 = size*7/16
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(dist2)
    turtle.right(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.right(90)
    turtle.forward(dist2)
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.left(90)
    turtle.forward(dist2)
    turtle.forward(dist/10)
    turtle.down()

def letterG(turtle, size):
    dist = size/4
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.left(180)
    turtle.circle(dist, 180)
    turtle.up()
    turtle.forward(dist*2)
    turtle.down()
    turtle.circle(dist, 180)
    turtle.forward(dist*2)
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.forward(dist)
    turtle.right(90)
    turtle.forward(dist)
    turtle.left(90)
    turtle.up()
    turtle.forward(dist/5)
    turtle.down()

def letterH(turtle, size):
    dist = size*7/16
    dist2 = size/2
    turtle.left(90)
    turtle.forward(size)
    turtle.up()
    turtle.backward(dist2)
    turtle.down()
    turtle.right(90)
    turtle.forward(dist)
    turtle.left(90)
    turtle.up()
    turtle.forward(dist2)
    turtle.down()
    turtle.right(180)
    turtle.forward(size)
    turtle.left(90)
    turtle.up()
    turtle.forward(dist2/10)
    turtle.down()

def letterI(turtle, size):
    pass

def letterJ(turtle, size):
    pass

def letterK(turtle, size):
    pass

def letterL(turtle, size):
    pass

def letterM(turtle, size):
    pass

def letterN(turtle, size):
    pass

def letterO(turtle, size):
    pass

def letterP(turtle, size):
    pass

def letterQ(turtle, size):
    pass

def letterR(turtle, size):
    pass

def letterS(turtle, size):
    pass

def letterT(turtle, size):
    pass

def letterU(turtle, size):
    pass

def letterV(turtle, size):
    pass

def letterW(turtle, size):
    pass

def letterX(turtle, size):
    pass

def letterY(turtle, size):
    pass

def letterZ(turtle, size):
    pass
