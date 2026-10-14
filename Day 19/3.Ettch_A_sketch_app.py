from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)

def backward():
    tim.back(10)

def left():
    tim.setheading(tim.heading()+10)

def right():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home() # placed the turtle to origin (0,0)
    tim.pendown()


screen.listen()

screen.onkey(key="w" , fun=forward)
screen.onkey(key="s" , fun=backward)
screen.onkey(key="a" , fun=left)
screen.onkey(key="d" , fun=right)
screen.onkey(clear , "c")



screen.exitonclick()