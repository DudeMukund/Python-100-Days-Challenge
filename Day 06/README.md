# Day 6: Functions & While Loops

## What I Learned Today

### Functions

Learned the basics of functions — a block of code that takes 
**input** and produces **output**, and can be reused multiple times.

**Two types of functions in Python:**

1. **Built-in functions** — already provided by Python (e.g., 
   `print()`). You just call them and pass the required parameters 
   inside the brackets.
2. **User-defined functions** — functions we create ourselves.

**How to create a function:**
```python
def function_name(parameter1, parameter2):
    # code goes here
```
- **`def`** stands for "definition" — it's how Python knows you're 
  starting a new function
- After `def`, we give the function a name, followed by parameters 
  in brackets

**Important — Indentation:**
Indentation (typically 4 spaces) is critical in Python. It tells 
Python which lines of code belong **inside** the function (or any 
block like a loop or conditional). Forgetting to indent properly 
results in an `IndentationError`.

### While Loops

A `while` loop keeps running **as long as its condition remains 
True**. The general flow is:
1. Check the condition
2. If True, run the code inside the loop
3. Go back and check the condition again
4. Repeat until the condition becomes False — only then does the 
   loop exit

If the condition never becomes False, the loop runs **infinitely**.

**Loop control keywords:**
- **`break`** — immediately exits the loop, stopping all further 
  iterations
- **`continue`** — skips the rest of the current iteration and moves 
  to the next one
- **`pass`** — does nothing; used as a placeholder when a statement 
  is syntactically required but no action is needed yet

## Mini Project
### Number Guessing Game
A simple game that generates a random number between 1 and 20, and 
challenges the user to guess it. After each guess, the program gives 
feedback — whether the guess was too high, too low, or correct — and 
keeps track of how many attempts it took to guess correctly.

## Key Takeaway
Functions are the building blocks for writing reusable, organized 
code — instead of repeating the same logic everywhere, I can now 
wrap it in a function and call it whenever needed. Understanding the 
difference between `break`, `continue`, and `pass` also cleared up a 
lot of confusion about controlling loop behavior precisely.