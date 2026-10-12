from turtle import Turtle, Screen

magic_turtle = Turtle()
screen = Screen()


magic_turtle.shape("turtle") # changeing apparenace
magic_turtle.color("DarkCyan")  # changeing colur of turtle
magic_turtle.pensize(13)  # changeing turtle  pen size
magic_turtle.pencolor("Red") # changeing pen color of turtle


# giving instruction to move:
for i in range(4):
    magic_turtle.forward(100)
    magic_turtle.left(90)

























screen.exitonclick() # scrren show till you close or you click on the shown screen