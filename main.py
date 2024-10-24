while True:
    time_left = int(input("How many seconds do you want to play the game for? "))
    if time_left > 0:
        print(time_left, "seconds")
        break

import turtle as trtl
import random

p = trtl.Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
shapes = ["arrow", "circle", "classic", "square", "triangle", "turtle"]
counter = 0
game_active = True

def randomize():
    color_turtle = colors[random.randint(0, len(colors) - 1)]
    shape_turtle = shapes[random.randint(0, len(shapes) - 1)]
    shape_size = random.randint(1, 5)
    p.fillcolor(color_turtle)
    p.shape(shape_turtle)
    p.shapesize(shape_size)

def turtle_move():
    if game_active:
        p.penup()
        p.goto(random.randint(-400, 400), random.randint(-300, 300))
        p.pendown()
        randomize()
        p.stamp()

def update_score():
    if game_active:
        score_display.clear()
        score_display.penup()
        score_display.goto(-150, 0)
        score_display.pendown()
        score_display.write(f"Score: {counter}", font=("Verdana", 30, "normal"))

def click(x, y):
    global counter
    if game_active:
        counter += 1
        turtle_move()
        update_score()

def countdown():
    global time_left, game_active
    time_display.clear()
    time_display.penup()
    time_display.goto(150, 0)
    time_display.pendown()
    time_display.write(f"Time: {time_left}", font=("Verdana", 30, "normal"))
    
    if time_left > 0:
        time_left -= 1
        wn.ontimer(countdown, 1000)
    else:
        game_active = False
        time_display.clear()
        time_display.write("Time's up!", font=("Verdana", 30, "normal"))
        wn.onclick(None)

score_display = trtl.Turtle()
score_display.hideturtle()

time_display = trtl.Turtle()
time_display.hideturtle()

turtle_move()
update_score()

wn = trtl.Screen()
wn.onclick(click)

countdown()

wn.mainloop()
