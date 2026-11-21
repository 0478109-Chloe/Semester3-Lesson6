# homework: in class, we drew one carrot inside our canvas
# TODO: by calling the draw_carrot() function, draw 10 carrots with random spawn positions inside the canvas.
# A hint has been given to you.
# website to run turtle is https://play.pyroom.app/playground

import turtle
import random

# ---------- Setup ----------
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0) # speed 0 is the fastest
t.pensize(1)
t.pencolor("green")
t.fillcolor("green")
screen.bgcolor("skyblue")
screen.setup(1000, 500)
#       x (width) is 1000 and y (height) is 500
#       x: -500 to 500        y: -250 to 250

# we are going to draw a beautiful garden today

# ground
t.goto(-500, 50)
t.begin_fill()
for i in range(4):
    t.forward(1000)
    t.right(90)
t.end_fill()


t.goto(0, 0)


# one carrot:
def draw_carrot():
    t.pencolor("black")
    t.fillcolor("orange")
    t.begin_fill()
    t.forward(30)
    t.right(100)
    t.forward(80)
    t.right(160)
    t.forward(80)
    t.end_fill()

    t.pensize(10)
    t.pencolor("lime")
    t.forward(30)
    t.forward(-30)
    t.setheading(0)
    t.forward(30)
    t.left(75)
    t.forward(30)
    t.setheading(0)
    t.pensize(1)

def teleport(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# draw 10 carrots
for i in range(10):
    teleport(random.randint(-500, 500), random.randint(-250, 85))
    draw_carrot()


def draw_potato():
    t.pencolor("ivory")
    t.fillcolor("goldenrod")
    t.begin_fill()
    t.circle(30)
    t.end_fill()


#draw 10 potatos
for i in range(10):
    teleport(random.randint(-500, 500), random.randint(-250, -50))
    draw_potato()

#make the sun appear on the top right corner
teleport(450,150)

# sun
t.pencolor("yellow")
t.fillcolor("yellow")
t.pensize(4)

t.begin_fill()
for i in range(36):
    t.forward(13)
    t.left(10)
    # the lines
    t.right(100)
    t.forward(80)
    t.forward(-80)
    t.left(100)
t.end_fill()


t.pencolor("black")
t.pensize(2)

# house:
def draw_house():
    t.fillcolor("orange")
    t.begin_fill()
    for i in range(2):
        t.forward(170)
        t.left(90)
        t.forward(130)
        t.left(90)
    t.end_fill()

# window:
def draw_window():
    t.fillcolor("lightblue")
    t.begin_fill()
    for i in range(2):
        t.forward(40)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()

# roof:
def draw_roof():
    t.fillcolor("brown")
    t.begin_fill()
    t.forward(200)
    t.left(160)
    t.forward(160)
    t.left(40)
    t.forward(160)
    t.left(160)
    t.end_fill()

# base of the house
teleport(0,40)
draw_house()

# two windows
teleport(20, 100)
draw_window()
teleport(110, 100)
draw_window()

# roof
teleport(35, 170)
draw_roof()













