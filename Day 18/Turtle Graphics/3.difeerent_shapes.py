from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.pencolor("black")
timmy.pensize(4)

# num =3
# while num <11:
#     angle = 360 /num
#     for i in range(num):
#         timmy.forward(100)
#         timmy.right(angle)
#     num += 1




#trinage
for i in range(3):
    timmy.forward(100)
    timmy.right(120)
    

#square
timmy.forward(100)
timmy.pencolor("green")
for i in range(4):
    timmy.right(90)
    timmy.forward(100)

#pentagon
timmy.pencolor("indigo")
for i in range(5):
    timmy.right(72)
    timmy.forward(100)

#hexagone
timmy.pencolor("orange")
for i in range(6):
    timmy.right(60)
    timmy.forward(100)

#heptagon
timmy.pencolor("pink")
for i in range(7):
    timmy.right(51.42)
    timmy.forward(100)

#octagon
timmy.pencolor("grey")
for i in range(8):
    timmy.right(45)
    timmy.forward(100)

#nonagon
timmy.pencolor("blue")
for i in range(9):
    timmy.right(40)
    timmy.forward(100)

#decagon
timmy.pencolor("red")
for i in range(10):
    timmy.right(36)
    timmy.forward(100)


screen.exitonclick()