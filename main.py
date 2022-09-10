import turtle
from turtle import Screen, Turtle, done

# TODO Create a snake body

screen = Screen()
screen.bgcolor("black")
snake_length = 3
body = []

y = 0
while y < 3:
    tur = Turtle(shape="square", visible=False)
    tur.color("white")
    tur.penup()
    tur.goto(-y * 15, 0)
    tur.showturtle()
    body.append(tur)
    y += 1


def xd():
    pass


def travel():
    n = 0
    while n < 1:
        x = 0
        while x < snake_length:
            body[x].forward(1)

            x += 1
        n += 1


def go_up():
    x = 0
    start_x, start_y = body[0].pos()
    if turtle.heading() == 0:
    while x < snake_length:
        bod_x, bod_y = body[x].pos()
        if bod_x >= start_x:
            body[x].setheading(90)
            x += 1

        else:
            while bod_x < start_x:
                print(start_x, start_y)
                print(bod_x, bod_y)
                print(" ")
                travel()
                bod_x, bod_y = body[x].pos()
    while True:
        travel()


def go_left():
    x = 0
    start_x, start_y = body[0].pos()

    while x < snake_length:
        bod_x, bod_y = body[x].pos()
        if bod_y >= start_y:
            body[x].setheading(180)
            x += 1

        else:
            while bod_y < start_y:
                print(start_x, start_y)
                print(bod_x, bod_y)
                print(" ")
                travel()
                bod_x, bod_y = body[x].pos()
    while True:
        travel()


def go_right():
    x = 0
    while x < snake_length:
        body[x].setheading(0)
        x += 1


def go_down():
    x = 0
    start_x, start_y = body[0].pos()

    while x < snake_length:
        bod_x, bod_y = body[x].pos()
        if bod_x >= start_x:
            body[x].setheading(270)
            x += 1

        else:
            while bod_x < start_x:
                print(start_x, start_y)
                print(bod_x, bod_y)
                print(" ")
                travel()
                bod_x, bod_y = body[x].pos()
    while True:
        travel()


screen.onkey(go_up, 'Up')
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_down, 'Down')

screen.listen()

travel()

screen.exitonclick()
