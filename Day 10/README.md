# Day 10: Functions with Outputs & Calculator

## What I Learned Today

### Docstrings
A **docstring** is a short description you write inside a function, right 
under the `def` line, using triple quotes. It explains what the function 
does, so anyone reading the code (including future me) doesn't have to 
guess.
```python
def add(a, b):
    '''Adds two numbers and returns the result'''
    return a + b
```

### Return Statement
Learned more about `return` this time:
- `return` sends a value **back** to whoever called the function, so I 
  can store it or use it in other calculations.
- It also **exits the function immediately**. Anything written after 
  `return` inside that function never runs.
- That's why any `print()` statement has to come **before** `return`. If 
  I put `print()` after `return`, it will never execute.

### Multiple Return Statements
A function can have more than one `return`. Depending on which 
condition is true, a different `return` runs, and the function stops 
right there. I used this idea while working with the leap year logic.

## Mini Project: Leap Year Checker
Wrote a function `is_leap_year(year)` that returns whether a year is a 
leap year or not, using nested conditions:
- Divisible by 4, but not by 100 → leap year
- Divisible by 100, but not by 400 → not a leap year
- Divisible by 400 → leap year

Good practice for using multiple `return` statements inside 
`if / else` blocks.

## Main Project: Calculator
Today's project wasn't very theory-heavy, it was more hands-on. I built 
a calculator that does more than a basic one.

How it works:
- I made separate functions for `add`, `subtract`, `multiply`, and 
  `divide`.
- The user enters the first number, picks an operation (`+`, `-`, `*`, 
  `/`), then enters the next number, and the result is printed.
- After each calculation, the user gets a choice:
  - type `y` to **keep calculating with the previous result**, or
  - type `n` to **start a brand new calculation** from scratch.
- When starting fresh, the screen gets cleared with a bunch of newlines 
  and the `calculator()` function calls itself again (recursion).

## Key Takeaway
Understood that `return` doesn't just give back a value, it also ends 
the function, so the order of `print()` and `return` really matters. 
Docstrings make functions easier to understand, and building the 
calculator showed me how small functions can work together to make one 
bigger program.