from turtle import Turtle
import random
move_dist = 20
UP =90
DOWN = 270
LEFT= 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head =self.segments[0]

    def create_snake(self):  
        x_position = 0
        for _ in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(x=x_position, y=0)
            x_position -= 20
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()

            self.segments[seg_num].goto(new_x,new_y)

        self.head.forward(move_dist)

    # def snake_food(self): ## making fodd
    #     t=Turtle()
    #     t.hide()
    #     t.goto(random.randint(-280, 280), random.randint(-280, 280))
    #     t.dot(10,"pink")

    # def game_is_on(self):   ## if snake touch wall
        
    #     if self.head.xcor() >300 or self.head.xcor() < -300 or self.head.ycor() >300 or self.head.ycor() < -300:
    #         return False
    #     else:
    #         return True

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)


