# Day 5: For Loops, Range & Iteration

## What I Learned Today

### For Loops
Learned how to iterate over collections using `for` loops.
fruits = ["Apple", "Peach","pear"]
```python
for fruit in fruits:
    print(fruit)
```

Here, `fruit` is the **iterator variable** — it represents each 
individual element in the `fruits` list, one at a time, as the loop 
goes through the entire collection.

### Range()
Explored the `range()` function for generating sequences of numbers 
to loop through.

- **`range(start, stop)`** — starts at `start`, and stops **one 
  before** `stop` (i.e., `stop` itself is not included)
- **`range(start, stop, step)`** — adds a **step** value, which 
  controls how many elements to skip between each iteration

For example, `range(0, 10, 2)` skips every other number, iterating 
through 0, 2, 4, 6, 8 instead of every single number.

## Mini Projects

### 1. Password Generator
Built a program that generates two types of passwords using letters, 
symbols, and numbers:

- **Easy Password** — follows a structured sequence: letters first, 
  then symbols, then numbers
- **Hard Password** — completely randomized, mixing letters, symbols, 
  and numbers together in no particular order

This project relied heavily on the `random` module, `for` loops, and 
lists to build and shuffle the password characters.

### 2. FizzBuzz
A classic programming exercise — the program loops through a range 
of numbers and:
- Prints "Fizz" if the number is divisible by 3
- Prints "Buzz" if the number is divisible by 5
- Prints "FizzBuzz" if divisible by both
- Otherwise, prints the number itself

## Key Takeaway
Understanding `for` loops and `range()` opened up a lot of 
possibilities for automating repetitive tasks. The Password Generator 
project was especially fun — combining loops, randomization, and 
lists together to build something genuinely useful.