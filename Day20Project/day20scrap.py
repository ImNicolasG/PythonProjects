from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
# screen.tracer(0)



snake = Snake()
game_is_on = True

while game_is_on:

    snake.move()

screen.exitonclick()