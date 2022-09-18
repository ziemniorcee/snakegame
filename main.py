from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")  # This will call the up function if"Left the " arrow key is pressed
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.update()
    if snake.wall():
        score.game_over()
        game_is_on = False


screen.exitonclick()
