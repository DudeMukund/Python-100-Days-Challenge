from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.clear()                                   # erase the old dot
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.dot(15, "red")                            # draw a new dot
        
        