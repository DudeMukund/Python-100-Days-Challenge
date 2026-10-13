
from turtle import Turtle , Screen ,colormode
import random
colormode(255) # for rgb

tim = Turtle()
screen = Screen()
tim.shape("turtle")

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
move = [ 0 , 90 , 180 ,270 ]

tim.speed("fast")
tim.pensize(15)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
    

for i in range(200):
    # tim.pencolor(random.choice(colours))
    tim.color(random_color())
    tim.setheading(random.choice(move))
    tim.forward(30)
    
    
screen.exitonclick()