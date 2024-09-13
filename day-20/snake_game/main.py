import time
from turtle import  Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
# Move the whole snake
while game_is_on: # run as long as it is true
    screen.update() # update the screen when a movement is made for the whole snake
    time.sleep(0.1) # control how fast it refreshes
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()

screen.exitonclick()
