# from turtle import Turtle, Screen
#
# timmy = Turtle() # construct a turtle object
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red","green")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvwidth) #retrieve object attribute
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# table.field_names(["Pokemon", "Type"])
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"],align="r")
table.add_column("Type",["Electric","Water","Fire"],align="r")
print(table)