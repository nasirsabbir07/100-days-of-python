import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_x = -235
start_y = -80

all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(start_x, start_y)
    all_turtles.append(new_turtle)
    start_y += 25

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle finished first")
            else:
                print(f"You've lost!! The {winning_color} turtle finished first")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    
    
screen.exitonclick()