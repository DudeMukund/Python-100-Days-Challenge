from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()



# score = 0

# pen = Turtle()
# pen.color("yellow")
# pen.penup()
# pen.hideturtle()
# pen.goto(4, 270)
# pen.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
# while snake.game_is_on():
while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()

    # if snake head is close to 15 pixel of food or even closer.
    if snake.head.distance(food) < 15:
        food.refresh()
        
        # score += 1
        # pen.clear()
        # pen.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))

    


        
screen.exitonclick()


#turtle.distance(x,y=none) --> it return disatnce b/w turtle and x in pixel