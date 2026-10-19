# Day 20 & 21: Snake Game (Inheritance and Turtle Graphics)

## What I Learned Today

The Snake game is big for a beginner, so the course split it into **7 steps**
across two days. I am combining Day 20 and Day 21 in one README because they
are the same project.

- **Day 20 (3 steps):** make the snake body, make it move, and control it with
  the keyboard.
- **Day 21 (4 steps):** generate the food, detect collision with the food,
  detect collision with the wall, detect collision with the tail, and keep a
  score.

### Concepts I learned
- **Inheritance**: just like a child gets genetics from parents, a class can
  get the attributes and methods of another class. If I have an `Animal`
  class and I make a `Dog` class, I pass `Animal` as the argument of `Dog`,
  and then `Dog` can use everything from `Animal`.
- **`super().__init__()`**: inside the child class, this calls the
  initialization code of the parent class, so the child gets the parent's
  attributes too. `super()` is a reference to the parent class.
- **Turtle graphics (much deeper)**: I started it on Day 16 and Day 19, but
  in these two days I learned a lot more. I now know how to make shapes,
  move them, listen to key presses and update the screen manually.
- **`screen.tracer(0)` and `screen.update()`**: I turn off the automatic
  animation and update the screen myself once per loop, so the snake moves
  smoothly.
- **`screen.listen()` and `screen.onkey()`**: connect arrow keys to the
  snake's `up`, `down`, `left` and `right` methods.
- **`turtle.distance()`**: returns the distance in pixels between a turtle
  and another turtle (or x, y). I used it for collision detection.

### How the project works
The project is split across files:
- `snake.py`: the `Snake` class. It builds the body segments, and has the
  methods `move()`, `extend()`, `up()`, `down()`, `left()` and `right()`.
  `snake.head` is the first segment and `snake.segments` is the full body.
- `food.py`: the `Food` class. It is a turtle that shows the food, and
  `refresh()` moves it to a new random place on the screen.
- `score_board.py`: the `ScoreBoard` class. `score_update()` adds to the
  score and `game_over()` shows the game over message.
- `main.py`: sets up the screen (600x600, black background), makes the
  `Snake`, `Food` and `ScoreBoard` objects, listens for the arrow keys, and
  runs the main game loop.

### The game loop (in `main.py`)
Every 0.1 seconds the loop updates the screen and moves the snake, then
checks three things:
1. **Food collision**: if the head is closer than 15 pixels to the food, the
   food moves to a new random place, the snake extends by one segment, and
   the score goes up.
2. **Wall collision**: if the head's x or y coordinate goes past 280, the game
   is over.
3. **Tail collision**: if the head is closer than 10 pixels to any segment
   of the body (`snake.segments[1:]`), the game is over.

Eat one fruit and get 1 score, eat two and get 2, and so on.

## My Own Ideas
- **Hitting the wall** was my own idea: checking the head's coordinates
  against the wall limit.
- **Attaching the snake bodies to each other**: I had a different idea about
  how to connect the segments, but I ended up using the course's way.

## Honest Reflection

The snake game is pretty huge for me because I am a beginner. About
**20 to 25%** of the work was mine. I would get a hint, try it myself,
and sometimes I was successful and sometimes I got confused. Even so, it
was a new experience and I am satisfied with myself. I did great.

One thing to be honest about: this is Day 20 and Day 21, but it took me
**four days** to finish, because I was lazy these days. I want to fix that
and be more consistent.

## Key Takeaway
Inheritance lets a child class reuse the parent class, and `super().__init__()`
is how the child sets up the parent part. Breaking a big project like Snake
into small steps (body, movement, food, collisions, score) made it possible
for me. Next time I want to write more of the code myself and keep a steady
pace every day.