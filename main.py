from turtle import Screen, Turtle

# TODO Create a snake body

screen = Screen()
screen.bgcolor("black")
snake = Turtle()
snake.color("white")
snake.shape("square")

print(snake.pos())

body = []
snake_length = 3
y = 1
while y < 3:
    tur = Turtle()
    tur.shape("square")
    tur.color("white")
    tur.penup()
    tur.goto(-y * 22, 0)
    body.append(tur)
    y += 1


while True:
    x = 1
    while x < snake_length:



screen.exitonclick()
