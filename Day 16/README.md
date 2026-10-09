# Day 16: OOP Basics + Coffee Machine (OOP Version)

## What I Learned Today

Today I started **Object-Oriented Programming (OOP)**. Before this, everything I wrote was *procedural programming* (step-by-step code with functions). Procedural is fine for small things, but for real-world problems OOP fits much better because it models things the way they exist in the real world.

### Core concepts
- **Class**: a blueprint. It describes what something has and what it can do.
- **Object**: an actual thing created from the blueprint. Also called an **instance**.
- **Attribute**: a variable that belongs to a class/object.
- **Method**: a function that belongs to a class.
- **How to use them**: create an object (`car = Car()`), access an attribute (`car.speed`), call a method (`car.drive()`).


## Project: Coffee Machine with Classes

In Day 15 I wrote the whole coffee machine myself using a `while` loop and functions. This time was different: my teacher gave me **ready-made classes** and I only had to **use** them, not write them.

### Files in the project
| File | Purpose |
|------|---------|
| `art.py` | The coffee logo |
| `menu.py` | `Menu` class: the list of drinks and finding a drink |
| `coffee_maker.py` | `CoffeeMaker` class: resources, report, checking resources, making coffee |
| `money_machine.py` | `MoneyMachine` class: payment handling and profit report |
| `main.py` | **My code**: connects everything together |

### How `main.py` works
- Creates one object from each class: `Menu()`, `CoffeeMaker()`, `MoneyMachine()`.
- Runs inside a `while` loop controlled by `is_coffee_macine_on`.
- Asks the user what they want, using `menu.get_items()` to show the options.
- `off` turns the machine off.
- `report` prints both the coffee maker's resources and the money machine's profit.
- Otherwise, `menu.find_drink()` looks up the drink. If it exists:
  1. `coffee_maker.is_resource_sufficient(drink)` checks the ingredients.
  2. `money_machine.make_payment(drink.cost)` handles the payment.
  3. `coffee_maker.make_coffee(drink)` makes the drink.
- A small `clear()` function clears the screen between rounds.

## Honest Reflection

This was an easy project, but a good one. At first I didn't understand what I was supposed to do, because I was used to writing everything from scratch. After going through the class descriptions (what each method takes and what it returns), it clicked, and I finished `main.py` successfully on my own.

Compared to Day 15, the `main.py` is much shorter and cleaner. All the messy logic (resources, money, menu) lives inside the classes, and `main.py` just calls methods. That's the real benefit of OOP.

## Key Takeaway
Using someone else's classes is a skill by itself: read what a class offers (its attributes and methods), understand what goes in and what comes out, and then connect the pieces. This is how real-world programming works, since most of the time we use code that other people wrote.