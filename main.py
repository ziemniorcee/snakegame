from turtle import Screen, Turtle

# TODO Create a snake body

screen = Screen()
screen.bgcolor("black")



body = []
snake_length = 3
y = 0
while y < 3:
    tur = Turtle(shape="square", visible=False)
    tur.color("white")
    tur.penup()
    tur.goto(-y * 15, 0)
    tur.showturtle()
    body.append(tur)
    y += 1

while True:
    x = 0
    while x < snake_length:
        body[x].forward(5)
        x += 1
    if body[0].xcor()+20 == screen.window_width() / 2:
        break

screen.exitonclick()
