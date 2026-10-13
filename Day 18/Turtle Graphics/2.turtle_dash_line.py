from turtle import Turtle , Screen

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
# for i in range(15):
#     timmy.forward(10)
#     timmy.pencolor("white")
#     timmy.forward(10)
#     timmy.pencolor("Green")

for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()












screen.exitonclick()
