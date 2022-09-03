from turtle import Turtle, Screen

import random

is_racing = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win?\nPurple, Blue, Green, Yellow, Orange, or Red?").lower()

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
y_coord = 125

racers = []


for color in colors:
    johnny = Turtle(shape="turtle")
    johnny.color(color)
    johnny.penup()
    johnny.goto(x=-230, y=y_coord)
    y_coord -= 50
    racers.append(johnny)

if user_bet:
    is_racing = True

while is_racing:

    for turtle in racers:
        if turtle.xcor() > 230:
            is_racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color.capitalize()} is the winner!")
            else:
                print(f"You've lost! {winning_color.capitalize()} is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()