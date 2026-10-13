# Day 18: Turtle Graphics & Hirst Dot Painting

## What I Learned Today

Today was all about **Turtle Graphics** in Python. It was a pretty vast and
good tutorial, and I got to see how many different ways turtle can be used.
For me it was genuinely cool, because this was my first time drawing things
with code.

### Turtle Basics
- Made a **square** with turtle for the first time
- Changed the **size** of the pen
- Changed the turtle's **shape** (triangle, rectangle, etc.) using `.shape()`
- Changed the **color** of the turtle and the pen/paint color

## Turtle Graphics Practice

### 1. Turtle Square
Drew a basic square using `forward()` and turning the turtle.

### 2. Turtle Dash Line
Made a dashed line by alternating between pen up and pen down.

### 3. Different Shapes
Started with a triangle, then drew a square on top of it, and kept going:
pentagon, hexagon, heptagon, octagon, nonagon, and decagon, each in its own color.

### 4. Random Walk
My favorite one. I built the random walk by myself, with just a small hint
about moving in the directions `0`, `90`, `180`, `270` and using `setheading()`.

### 5. Spirograph
Also really enjoyed this one. I only needed the hint of using a circle, and
then I figured out the rest on my own.

### 6. Square Spirograph
This one is my own project. I made it completely by myself by using a square
instead of a circle.

## Main Project: Hirst Dot Painting

Today's project was creating a dot painting like the famous Hirst-style art.

**How it works:**
1. I picked a painting image (`paint.jpg`)
2. Installed the **colorgram** package, which extracts colors from an image
3. Extracted **30 RGB colors** from the painting
4. Stored them in a list of tuples in `(r, g, b)` format
5. Used turtle to draw a grid of **10 x 10 = 100 dots**, each with a
   random color from that list


## Key Takeaway
I'm not proud of today, but I'm satisfied. It wasn't a 100% day, but it was a
good, steady one. Building the random walk and the square spirograph on my own
felt great, and using `colorgram` to pull real colors out of an image and turn
them into a dot painting tied the whole turtle lesson together.