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

def draw_spirograph(gap):
    for i in range(360 // gap):
        timmy.color(random_colour())
        timmy.circle(150)
        timmy.setheading(timmy.heading() + gap)

draw_spirograph(5)


screen.exitonclick()


# print(timmy.heading())   # 0.0 at the start
# timmy.left(90)
# print(timmy.heading())   # 90.0
# timmy.setheading(180)    # now faces west
#print(timmy.heading())  #180