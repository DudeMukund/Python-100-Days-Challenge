# Day 15: Coffee Machine

## What I Learned Today

No new theory today. Today was project work: I built a **Coffee Machine
program** that takes an order, checks the ingredients, takes coins,
gives change, and tracks profit. The big thing I learned was **how to
use functions and when to use them**, and I used them properly in a
real project for the first time.

### How the project works
- `MENU` is a nested dictionary holding each drink's ingredients and
  cost. `resources` holds what the machine has left.
- The user types `espresso`, `latte` or `cappuccino`. `.lower()` on the
  input means capital letters also work.
- `resourse_avilable()` checks every ingredient and prints which one is
  missing if there isn't enough.
- `process_coins()` asks for quarters, dimes, nickels and pennies and
  returns the total money inserted.
- `check_transaction()` refunds the money if it isn't enough. Otherwise
  it prints the change and adds the cost to `profit` using `global`.
- `make_cofee()` deducts the ingredients from `resources` and serves
  the drink.
- Typing `report` prints the remaining water, milk, coffee and the
  profit. Typing `off` breaks the loop and stops the machine. Any other
  input prints "Invalid choice, please try again."

## Honest Reflection

I built this on my own, and I am happy with it. On the Day 14 project my
regret was not using functions. Today I fixed that: every job (checking
resources, taking coins, handling payment, making the coffee) has its
own function, and the main `while` loop is short and easy to read.

I know it is not perfect yet. Some function names have typos
(`resourse_avilable`, `make_cofee`), the change can show float noise
like `0.30000000000000004` because I did not use `round()`, and typing
a letter at the coin prompt crashes the program with a `ValueError`.

## Key Takeaway
A function should do one job, and the main loop should only call
functions and not hold all the logic. The next improvement is
robustness: use `round(total - cost, 2)` for money, validate the coin
input with `try`/`except`, and choose clear function names so the code
is easy to read later.