import time
from turtle import Turtle, Screen
from snake import Snake

screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

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


screen.exitonclick()
