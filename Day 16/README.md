# Day 16: OOP Basics + Coffee Machine (OOP Version)

## What I Learned Today

Today I started **Object-Oriented Programming (OOP)**. Before this, everything I wrote was *procedural programming* (step-by-step code with functions). Procedural is fine for small things, but for real-world problems OOP fits much better because it models things the way they exist in the real world.

### Core concepts
- **Class**: a blueprint. It describes what something has and what it can do.
- **Object**: an actual thing created from the blueprint. Also called an **instance**.
- **Attribute**: a variable that belongs to a class/object.
- **Method**: a function that belongs to a class.
- **How to use them**: create an object (`car = Car()`), access an attribute (`car.speed`), call a method (`car.drive()`).

### `__init__` and `self`
- `__init__` is a special method that runs automatically when an object is created. It's where I set up the object's attributes.
- `self` is a reference to the current object. Object attributes are written as `self.name = name` inside `__init__`.

### Class variable vs object variable
- **Class variable**: defined in the class body, shared by all objects of that class.
- **Object variable**: defined with `self` inside `__init__`, separate for each object.
- If both have the same name, the **object variable takes precedence** over the class variable.

### Decorators and static methods
- Learned about the `@staticmethod` decorator. A static method doesn't receive `self`, because it doesn't need access to any particular object.

### Abstraction and Encapsulation
- **Abstraction**: hide the complicated inner details and show the user only what's important.
- **Encapsulation**: keep the data (attributes) and the methods that work on it together in one "capsule", the class.

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