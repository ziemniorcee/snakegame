from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")

head = Turtle(shape="square")
head.color("white")
body_length = 2


def create_body():
    snake_body = []
    x = 0
    while x < 2:
        tur = Turtle(shape="square", visible=False)
        tur.color("white")
        tur.penup()
        tur.goto(-x * 15, 0)
        tur.speed('fastest')
        tur.showturtle()
        snake_body.append(tur)
        x += 1
    return snake_body


def follow():
    x = 0
    while x < body_length:
        if head.heading() != body[x].heading():


def


def travel():
    head.forward(1)
    screen.ontimer(travel, 10)


screen.onkey(lambda: head.setheading(90), 'Up')
screen.onkey(lambda: head.setheading(180), 'Left')
screen.onkey(lambda: head.setheading(0), 'Right')
screen.onkey(lambda: head.setheading(270), 'Down')

body = create_body()

screen.listen()

travel()
follow()
screen.exitonclick()
