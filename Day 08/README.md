# Day 8: Functions with Inputs & Caesar Cipher

## What I Learned Today

### Functions with Multiple Inputs
Learned how to create functions that take more than one input at a 
time — instead of just a single parameter, functions can accept 
multiple values and use all of them inside the logic.

### Parameters vs Arguments
This one took me a bit to wrap my head around, but here's how I 
understand it now:
- A **parameter** is just the *name* you give to an input inside the 
  function definition (like a placeholder)
- An **argument** is the *actual value* you pass in when you call 
  the function

So basically, the parameter is the label, and the argument is the 
real data that fills that label.

## Mini Projects (More About Functions)

### 1. Life in Weeks
A program where you enter your current age, and assuming an average 
lifespan of 90 years, it calculates how many weeks you have 
remaining in your life. Kind of a wake-up-call kind of project, 
honestly.

### 2. True Love Calculator
Takes two names as input, and calculates a "true love score" by 
counting how many times the letters from the word **TRUE** and 
**LOVE** appear across both names combined. A fun, silly little 
project but good practice with string manipulation and loops.

## Main Project: Caesar Cipher

Today's main project was building a Caesar Cipher — both the 
**encoding** and **decoding** parts.

Here's how it works: I first built an `encode` function, then a 
`decode` function. You give it a message and a shift number, and:
- The **encode** function shifts every letter forward by that number 
  to scramble the message
- The **decode** function shifts it back by the same number to 
  reveal the original message

It was genuinely satisfying to see a real message get encoded into 
gibberish and then correctly decoded back using the same shift 
number.

## Key Takeaway
Understanding the difference between parameters and arguments made a 
lot of earlier confusion click into place. And building the Caesar 
Cipher really tied together everything about functions, loops, and 
string manipulation into one solid project.