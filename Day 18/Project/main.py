from turtle import Turtle , Screen , colormode
import random
import colorgram

rgb_colors = []
# get the 30 unqiue rgb colors and stoue in rgb_colors
colors = colorgram.extract("Day 18/Project/paint.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors .append((r,g,b))



colormode(255) 
tim = Turtle()
screen = Screen()
tim.speed("fast")
tim.hideturtle()# hid turtle

tim.penup()


tim.setheading(225) # changing the direction 255 degrre
tim.forward(320)
tim.setheading(0)


no_of_dots = 100
for i in range(1 ,no_of_dots+1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)
    if i % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen.exitonclick()