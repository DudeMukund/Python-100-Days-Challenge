# Day 19: Multiple Turtles, Keyboard Events & Turtle Race Game

## What I Learned Today

### Making Multiple Turtles
`Turtle` is a **class**, so I can create as many **objects** from it as I want. In Day 18 I played with only one turtle, but today I made many of them, each with its own color, position, and movement.

### Positioning Each Turtle
- `penup()` so the turtle does not draw a line when it moves
- `goto(x, y)` to place it at an exact position
- Increasing `y` a little in every loop step puts the turtles in separate rows

### Controlling the Turtle with the Keyboard
To move the turtle with key presses, I need two things from the `Screen`:
1. `screen.listen()` makes the screen start **listening** for keyboard events
2. `screen.onkey(function, "key")` connects a key to a function

```python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(move_forward, "a")
screen.exitonclick()
```
Now when I press `a`, the turtle moves forward by 10.

Important: I pass the function **without brackets** (`move_forward`, not `move_forward()`), because I want the screen to call it later when the key is pressed, not run it right now.

### Useful Screen Methods
- `screen.setup(width=500, height=400)` sets the window size
- `screen.textinput(title, prompt)` shows a popup box to take input from the user
- `screen.exitonclick()` keeps the window open until I click on it
- `screen.bye()` closes the window

## Main Project: Turtle Race Game
Today's project was a **turtle race**. The user bets on a color, six turtles race across the screen, and the game tells if the bet won or lost.

How it works:
- A popup asks the user: *Which turtle will win the race?*
- Six turtles (red, orange, yellow, green, blue, purple) are created in a loop and lined up at the starting line.
- If the user typed a valid color, the race starts. Otherwise the game prints a message and closes.
- Inside a `while` loop, every turtle moves forward by a **random distance** (`random.randint(0, 10)`).
- When any turtle crosses `x > 230`, it is the winner.
- The game compares the winning color with the user's bet and prints **won** or **lost**.

Things I practiced here:
- Creating multiple objects from one class
- Storing objects in a list and looping through them
- `while` loop with a flag variable (`is_race_on`)
- `random.randint()` for unpredictable movement
- `xcor()` to read the turtle's x position
- `pencolor()` to get the color of the winning turtle
- `.lower()` on the input so `"Red"` and `"red"` both work


## Key Takeaway
Since `Turtle` is a class, I can create many turtle objects, each with its own state. With `screen.listen()` and `screen.onkey()`, the program can react to keyboard presses. Combining these ideas with loops, lists, and `random` gave me a working turtle race game. I was not super excited about turtle today, but I still made progress and finished the project.