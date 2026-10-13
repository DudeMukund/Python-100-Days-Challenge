from turtle import Turtle , Screen , colormode
import random
colormode(255)

timmy = Turtle()
screen = Screen()
timmy.pensize(2)
timmy.speed("fastest")
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_square_spirograph(gap):
    for i in range(360 // gap):
        timmy.color(random_colour())
        timmy.forward(100)
        timmy.right(90)
        timmy.forward(100)
        timmy.right(90)
        timmy.forward(100)
        timmy.right(90)
        timmy.forward(100)
        timmy.setheading(timmy.heading() + gap)

draw_square_spirograph(5)


screen.exitonclick()
