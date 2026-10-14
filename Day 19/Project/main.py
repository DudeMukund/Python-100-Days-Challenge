from turtle import  Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter a color ("red","orange","yellow","green","blue","purple") :  ').lower()
colors = ["red","orange","yellow","green","blue","purple"]
all_turtle = []


y_position =-75
for i in range(6):
    t1 = Turtle(shape="turtle")
    t1.color(colors[i])
    t1.penup()
    t1.goto(x=-220,y=y_position)
    y_position +=30
    all_turtle.append(t1)



if user_bet in colors:
    is_race_on=True

else:
    print("you typed wrong color")
    screen.bye()

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle is the winner")
                is_race_on = False
            else:
                print(f"you've lost! the {winning_color} turtle is the winner!")
                is_race_on = False

        random_disantce = random.randint(0,10)
        turtle.forward(random_disantce)
    

screen.exitonclick()