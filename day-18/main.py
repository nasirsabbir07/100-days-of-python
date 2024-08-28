from turtle import Turtle, Screen
import random
import string

tim = Turtle() #construct the object
string_size = 6

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

## Draw a dashed line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# def draw_shape(num_side):
#     """draw shapes consisting from three sides to ten"""
#     angle = 360 / num_side
#     for _ in range(num_side):
#         color_string = "".join(random.choices("0123456789abcdef", k=string_size))
#         color_code = "#" + color_string
#         tim.color(color_code)
#         tim.forward(100)
#         tim.right(angle)

# for sides in range(3,11):
#     draw_shape(sides)

# TODO: create a  random walk for the turtle
# tim.pensize(15)
# movement = [tim.forward, tim.backward, tim.left, tim.right]
tim.speed("fastest")
# def walk():
#     for _ in range(300):
#         color_string = "".join(random.choices("0123456789abcdef", k=string_size))
#         color_code = "#" + color_string
#         tim.color(color_code)
#         move_function = random.choice(movement)
#         if move_function in [tim.left, tim.right]:
#             move_function(90)
#         else:
#             move_function(30)
# walk()

def random_color():
    color_string = "".join(random.choices("0123456789abcdef", k=string_size))
    color_code = "#" + color_string
    return color_code

# TODO: Draw a spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)
screen = Screen()
screen.exitonclick()