import turtle
import time
import random

#created delay for refresh rate
delay = 0.1

#screen setup
screen = turtle.Screen()
screen.title("""Water slang     By: Chad Hoosain""")
screen.bgcolor("turquoise")
screen.setup(width=600, height=600)
screen.tracer(0)

# line boundary
l = turtle.Turtle()
l.hideturtle()
l.speed(25)
l.color("white")
l.pensize(5)
l.penup()
l.left(90)
l.forward(300)
l.pendown()
l.left(90)
l.forward(300)
l.left(90)
l.forward(600)
l.left(90)
l.forward(600)
l.left(90)
l.forward(600)
l.left(90)
l.forward(300)



#snake head
slangkop = turtle.Turtle()
slangkop.speed(0)   # speed of module, fastest speed
slangkop.shape("square")
slangkop.color("yellow")
slangkop.penup()
slangkop.goto(0,0)
slangkop.direction = "stop"
slangkop.speed = 1

#snakefood
food = turtle.Turtle()
food.speed(0)   # speed of module, fastest speed
food.shape("turtle")
food.color("lime green")
food.penup()
food.goto(0,100)

body_segments = []

def go_up():
    if slangkop.direction != "down":
        slangkop.direction = "up"
def go_down():
    if slangkop.direction != "up":
        slangkop.direction = "down"
def go_left():
    if slangkop.direction != "right":
        slangkop.direction = "left"
def go_right():
    if slangkop.direction != "left":
        slangkop.direction = "right"


def movement():
    if slangkop.direction == "up":
        y = slangkop.ycor()
        slangkop.sety(y + 20) # this will move the snake up 20incr each time
    if slangkop.direction == "down":
        y = slangkop.ycor()
        slangkop.sety(y - 20) # this will move the snake up 20incr each time
    if slangkop.direction == "left":
        x = slangkop.xcor()
        slangkop.setx(x - 20) # this will move the snake up 20incr each time
    if slangkop.direction == "right":
        x = slangkop.xcor()
        slangkop.setx(x + 20) # this will move the snake up 20incr each time

#keybindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")


#main game loop, so game is in frames at a high speed rate.
while True:
    screen.update()

    # Check for a collision with the border
    if slangkop.xcor() > 299 or slangkop.xcor() < -299 or slangkop.ycor() > 299 or slangkop.ycor() < -299:
        time.sleep(0.5)
        slangkop.goto(0,0)
        slangkop.direction = "stop"

        for new_body in body_segments:
            new_body.goto(1000,1000)
        #Clears body segment list
        body_segments.clear()

    #used if statement to check for a collision with the food
    if slangkop.distance(food) < 20:#move food to random spot on the screen
        slangkop.speed += 2
        # since screen is 600x600 you need to /2 to get each halves and -10 to not let food go off screen
        x = random.randint(-290, 290)
        y = random.randint(-290,290)
        food.goto(x, y)

    #Added a segment for snake growth
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("orange")
        new_body.penup()
        body_segments.append(new_body)

    #move the end segments first in reverse order
    for i in range(len(body_segments)-1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)

    #move segment 0 to where the head is
    if len(body_segments) > 0:
        x = slangkop.xcor()
        y = slangkop.ycor()
        body_segments[0].goto(x, y)

    #function for the movement of the snake
    movement()

    #Check for head collision with the body segments
    for new_body in body_segments:
        if new_body.distance(slangkop) < 20:
            time.sleep(0.5)
            slangkop.goto(0,0)
            slangkop.direction = "stop"
            for new_body in body_segments:
                new_body.goto(1000, 1000)
            # Clears body segment list
            body_segments.clear()

    time.sleep(delay)

screen.mainloop()