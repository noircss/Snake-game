# Created by NOiRcs with the help of TokyoEdtech on youtube.com
# My first ever pygame


import turtle
import time
import random

delay = 0.1

# screen
wn = turtle.Screen()
wn.title("snake game by noircs")
wn.bgcolor("white")
wn.setup(width=700, height=700)
wn.tracer(0)  # turns off screen updates

# head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# snake food
# head
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# functions


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")

wn.onkeypress(go_down, "s")

wn.onkeypress(go_left, "a")

wn.onkeypress(go_right, "d")

# main game loop
while True:
    wn.update()


    #check for a collision with the border
    if head.xcor()>350 or head.xcor()<-350 or head.ycor()>350 or head.ycor()<-350:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"


    # check for collision with the food
    if head.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

    # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)


    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
        pass



    move()


    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

    #hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            #clear the segments list
            segments.clear()

    time.sleep(delay)

    
wn.mainloop()
