import math


def space(turtle, size):
    turtle.up()
    turtle.forward(size / 4)
    turtle.down()


def letterA(turtle, size):
    turtle.left(75)
    dist = size / math.cos(math.radians(15))
    turtle.forward(dist)
    turtle.right(150)
    turtle.forward(dist / 2)
    turtle.right(105)
    dist2 = size * math.tan(math.radians(15))
    turtle.forward(dist2)
    turtle.up()
    turtle.backward(dist2)
    turtle.down()
    turtle.left(105)
    turtle.forward(dist / 2)
    turtle.left(75)
    turtle.up()
    turtle.forward(size / 20)
    turtle.down()


def letterB(turtle, size):
    dist = size / 5
    dist2 = size / 4
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
    turtle.forward(dist2 + dist / 4)
    turtle.down()


def letterC(turtle, size):
    dist = size / 4
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.right(180)
    turtle.circle(dist, 180)
    turtle.up()
    turtle.forward(size / 2)
    turtle.down()
    turtle.circle(dist, 180)
    turtle.forward(dist * 2)
    turtle.up()
    turtle.forward(dist)
    turtle.left(90)
    turtle.forward(dist * 2.2)
    turtle.down()


def letterD(turtle, size):
    dist = size / 2
    dist2 = size * 3 / 40
    turtle.forward(dist2)
    turtle.circle(dist, 180)
    turtle.forward(dist2)
    turtle.left(90)
    turtle.forward(size)
    turtle.up()
    turtle.left(90)
    turtle.forward(dist * 1.2)
    turtle.down()


def letterE(turtle, size):
    dist = size / 2
    dist2 = dist * 7 / 8
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
    turtle.forward(dist / 10)
    turtle.down()


def letterF(turtle, size):
    dist = size / 2
    dist2 = dist * 7 / 8
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
    turtle.forward(dist / 10)
    turtle.down()


def letterG(turtle, size):
    dist = size / 4
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.left(180)
    turtle.circle(dist, 180)
    turtle.up()
    turtle.forward(dist * 2)
    turtle.down()
    turtle.circle(dist, 180)
    turtle.forward(dist * 2)
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.forward(dist)
    turtle.right(90)
    turtle.forward(dist)
    turtle.left(90)
    turtle.up()
    turtle.forward(dist / 5)
    turtle.down()


def letterH(turtle, size):
    dist = size * 7 / 16
    dist2 = size / 2
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
    turtle.forward(dist2 / 10)
    turtle.down()


def letterI(turtle, size):
    dist = size * 3 / 40
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.left(90)
    turtle.forward(size)
    turtle.up()
    turtle.backward(size)
    turtle.right(90)
    turtle.forward(dist * 5 / 3)
    turtle.down()


def letterJ(turtle, size):
    dist = size / 4
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.right(180)
    turtle.circle(dist, 180)
    turtle.forward(dist * 3)
    turtle.left(90)
    turtle.forward(dist * 2)
    turtle.left(90)
    turtle.up()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(dist * 2.2)
    turtle.down()


def letterK(turtle, size):
    angle = 40
    dist = size / 2
    dist2 = dist / math.cos(math.radians(angle))
    turtle.left(90)
    turtle.forward(dist)
    turtle.right(angle)
    turtle.forward(dist2)
    turtle.left(90 + angle)
    turtle.up()
    turtle.forward(dist * math.tan(math.radians(angle)))
    turtle.left(90)
    turtle.down()
    turtle.forward(dist)
    turtle.left(angle)
    turtle.forward(dist2)
    turtle.left(90 - angle)
    turtle.up()
    turtle.forward(dist / 10)
    turtle.down()


def letterL(turtle, size):
    turtle.left(90)
    turtle.forward(size)
    turtle.up()
    turtle.backward(size)
    turtle.down()
    turtle.right(90)
    turtle.forward(size * 7 / 16)
    turtle.up()
    turtle.forward(size / 20)
    turtle.down()


def letterM(turtle, size):
    angle = 30
    dist = 0.5 * size / math.cos(math.radians(angle))
    turtle.left(90)
    turtle.forward(size)
    turtle.right(180 - angle)
    turtle.forward(dist)
    turtle.left(2 * (90 - angle))
    turtle.forward(dist)
    turtle.right(180 - angle)
    turtle.forward(size)
    turtle.left(90)
    turtle.up()
    turtle.forward(size / 20)
    turtle.down()


def letterN(turtle, size):
    angle = 25
    dist = size / math.cos(math.radians(angle))
    turtle.left(90)
    turtle.forward(size)
    turtle.right(180 - angle)
    turtle.forward(dist)
    turtle.left(180 - angle)
    turtle.forward(size)
    turtle.up()
    turtle.backward(size)
    turtle.right(90)
    turtle.forward(size / 20)
    turtle.down()


def letterO(turtle, size):
    dist = size / 4
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.right(180)
    turtle.circle(dist, 180)
    turtle.forward(dist * 2)
    turtle.circle(dist, 180)
    turtle.forward(dist * 2)
    turtle.up()
    turtle.forward(dist)
    turtle.left(90)
    turtle.forward(dist * 2.2)
    turtle.down()


def letterP(turtle, size):
    dist = size / 2
    dist2 = size / 5
    dist3 = size / 4
    turtle.left(90)
    turtle.forward(dist)
    turtle.right(90)
    turtle.forward(dist2)
    turtle.circle(dist3, 180)
    turtle.forward(dist2)
    turtle.left(90)
    turtle.forward(dist)
    turtle.up()
    turtle.forward(dist)
    turtle.left(90)
    turtle.forward(dist)
    turtle.down()


def letterQ(turtle, size):
    dist = size / 4
    dist2 = size / 10
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.right(180)
    turtle.circle(dist, 135)
    turtle.right(75)
    turtle.up()
    turtle.backward(dist2)
    turtle.down()
    turtle.forward(2 * dist2)
    turtle.up()
    turtle.backward(dist2)
    turtle.down()
    turtle.left(75)
    turtle.circle(dist, 45)
    turtle.forward(dist * 2)
    turtle.circle(dist, 180)
    turtle.forward(dist * 2)
    turtle.up()
    turtle.forward(dist)
    turtle.left(90)
    turtle.forward(dist * 2.2)
    turtle.down()


def letterR(turtle, size):
    dist = size / 2
    dist2 = size / 5
    dist3 = size / 4
    angle = math.degrees(math.atan((dist2 + dist3) / dist))
    turtle.left(90)
    turtle.forward(dist)
    turtle.right(90)
    turtle.forward(dist2)
    turtle.circle(dist3, 180)
    turtle.forward(dist2)
    turtle.left(90)
    turtle.forward(dist)
    turtle.left(angle)
    turtle.forward(dist / math.cos(math.radians(angle)))
    turtle.left(90 - angle)
    turtle.up()
    turtle.forward(dist / 10)
    turtle.down()


def letterS(turtle, size):
    dist = size / 4
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.right(180)
    turtle.circle(dist, 270)
    turtle.right(180)
    turtle.circle(dist, -270)
    turtle.right(180)
    turtle.up()
    turtle.forward(3 * dist)
    turtle.left(90)
    turtle.forward(dist / 5)
    turtle.down()


def letterT(turtle, size):
    dist = size * 7 / 16
    dist2 = dist / 2
    turtle.up()
    turtle.forward(dist2)
    turtle.down()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.up()
    turtle.backward(dist2)
    turtle.down()
    turtle.forward(dist)
    turtle.right(90)
    turtle.up()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 20)
    turtle.down()


def letterU(turtle, size):
    dist = size / 4
    dist2 = 3 * dist
    turtle.left(90)
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.right(180)
    turtle.circle(dist, 180)
    turtle.forward(dist2)
    turtle.left(90)
    turtle.up()
    turtle.forward(2 * dist)
    turtle.down()
    turtle.left(90)
    turtle.forward(dist2)
    turtle.up()
    turtle.forward(dist)
    turtle.left(90)
    turtle.forward(2.2 * dist)
    turtle.down()


def letterV(turtle, size):
    angle = 15
    dist = size / math.cos(math.radians(angle))
    turtle.up()
    turtle.left(90)
    turtle.forward(size)
    turtle.down()
    turtle.right(180 - angle)
    turtle.forward(dist)
    turtle.left(180 - 2 * angle)
    turtle.forward(dist)
    turtle.right(180 - angle)
    turtle.up()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 20)
    turtle.down()


def letterW(turtle, size):
    angle = 12
    angle2 = 180 - angle
    angle3 = 180 - 2 * angle
    dist = size / math.cos(math.radians(angle))
    dist2 = dist / 2
    turtle.left(90)
    turtle.up()
    turtle.forward(size)
    turtle.down()
    turtle.right(angle2)
    turtle.forward(dist)
    turtle.left(angle3)
    turtle.forward(dist2)
    turtle.right(angle3)
    turtle.forward(dist2)
    turtle.left(angle3)
    turtle.forward(dist)
    turtle.right(angle2)
    turtle.up()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 20)
    turtle.down()


def letterX(turtle, size):
    angle = 27
    angle2 = 90 - angle
    angle3 = 90 + angle
    dist = size / math.cos(math.radians(angle))
    turtle.left(angle2)
    turtle.forward(dist)
    turtle.left(angle3)
    turtle.up()
    turtle.forward(size * math.tan(math.radians(angle)))
    turtle.down()
    turtle.left(angle3)
    turtle.forward(dist)
    turtle.left(angle2)
    turtle.up()
    turtle.forward(size/20)
    turtle.down()

def letterY(turtle, size):
    angle = 27
    angle2 = 90+angle
    dist = 0.5 *size * math.tan(math.radians(angle))
    dist2= size/2
    dist3 = 0.5*size / math.cos(math.radians(angle))
    turtle.up()
    turtle.forward(dist)
    turtle.down()
    turtle.left(90)
    turtle.forward(size/2)
    turtle.left(angle)
    turtle.forward(dist3)
    turtle.right(angle2)
    turtle.up()
    turtle.forward(2*dist)
    turtle.down()
    turtle.right(angle2)
    turtle.forward(dist3)
    turtle.left(angle)
    turtle.up()
    turtle.forward(dist2)
    turtle.left(90)
    turtle.forward(dist)
    turtle.forward(dist2/10)
    turtle.down()


def letterZ(turtle, size):
    angle= 27
    angle2 = 90 + angle
    dist = size * math.tan(math.radians(angle))
    dist2 = size / math.cos(math.radians(angle))
    turtle.left(90)
    turtle.up()
    turtle.forward(size)
    turtle.down()
    turtle.right(90)
    turtle.forward(dist)
    turtle.right(angle2)
    turtle.forward(dist2)
    turtle.left(angle2)
    turtle.forward(dist)
    turtle.up()
    turtle.forward(size/20)
    turtle.down()


characters = {
    ' ': space,
    'A': letterA,
    'B': letterB,
    'C': letterC,
    'D': letterD,
    'E': letterE,
    'F': letterF,
    'G': letterG,
    'H': letterH,
    'I': letterI,
    'J': letterJ,
    'K': letterK,
    'L': letterL,
    'M': letterM,
    'N': letterN,
    'O': letterO,
    'P': letterP,
    'Q': letterQ,
    'R': letterR,
    'S': letterS,
    'T': letterT,
    'U': letterU,
    'V': letterV,
    'W': letterW,
    'X': letterX,
    'Y': letterY,
    'Z': letterZ,
}


def write(turtle, size, string):
    upper_string = string.upper()
    for char in upper_string:
        characters[char](turtle, size)
