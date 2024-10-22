import turtle as trtl
import random

p = trtl.Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
shapes = ["arrow", "circle", "classic", "square", "triangle", "turtle"]
counter = 0

def randomize():
    color_turtle = colors[random.randint(0, len(colors) - 1)]
    shape_turtle = shapes[random.randint(0, len(shapes) - 1)]
    shape_size = random.randint(1, 10)
    p.fillcolor(color_turtle)
    p.shape(shape_turtle)
    p.shapesize(shape_size)

def turtle_move(x, y):
    p.penup()
    p.goto(random.randint(-400, 400), random.randint(-300, 300))
    p.pendown()
    randomize()

def click(x, y):
    global counter
    counter += 1
    turtle_move(x, y)

#random teleport
turtle_move(0, 0)

#click
p.onclick(click)

wn = trtl.Screen()
wn.mainloop()
