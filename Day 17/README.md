# Day 17: Quiz Game (Object Oriented Programming)

## What I Learned Today

Today was my first real step into **object oriented programming (OOP)**. On
Day 16 I only learned how to *use* objects: how to make an object and how to
access its attributes and methods. Today I learned how to **make my own
class**, and then I used it to build a project, the **Quiz Brain** game.

### Concepts I learned (notes are in `OOPS/oops_1.ipynb`)
- **Class**: a blueprint for making objects. I now know how to write one
  myself, not just use one.
- **Object / instance**: a real thing made from a class.
- **Attribute**: a variable that lives inside a class.
- **Method**: a function that lives inside a class. Attribute and method are
  just different names for variable and function when they are under a class.
- **`__init__` (constructor)**: this is very important. It runs automatically
  as soon as an object is created. Inside it I set up the attributes (using
  `self`), and those can then be used anywhere in the class and from the
  object outside the class.
- **`self`**: a reference to the current object.
- **Static method**: when a function inside a class does not need the `self`
  argument, I can use the `@staticmethod` decorator.
- **Abstraction and encapsulation**: understood the basic idea of both.

I wrote all of these concepts in a Jupyter notebook (inside VS Code) so I
can come back and read them later. It also helped me get more familiar with
Jupyter.

### How the project works
The project is split across files:
- `data.py`: the `question_data` list with 12 True/False questions.
- `question_model.py`: the `Question` class. Its `__init__` takes the
  question `text` and the `answer` and stores them as attributes.
- `quiz_brain.py`: the `QuizBrain` class, which runs the quiz. It stores
  `question_number`, `question_list` and `score` in `__init__`, and has
  three methods:
  - `still_has_question()`: checks if questions are left. When they run out,
    it prints the final score and the verdict, then returns `False`.
  - `next_question()`: picks the current question, asks the user, and sends
    the answer to `check_answer()`.
  - `check_answer()`: compares the user's answer with the real answer, adds
    1 to the score if it is right, then prints the right answer and the
    current score (like `5/8`).
- `main.py`: loops over `question_data`, makes a `Question` object for each
  one, puts them in `question_bank`, makes a `QuizBrain` object, and runs
  `while quiz.still_has_question(): quiz.next_question()`.

### Things I handled
- `.capitalize()` on the input, so `true`, `TRUE` and `True` all work.
- After the 12th question, the game shows how many I got right out of 12.

### My own idea
The score judging at the end was **my own idea**, I added it on top of the
course project:
- score above 7: "you are smart"
- score above 4: "you are Average"
- otherwise: "you are dumb!"

## Honest Reflection

OOP is very difficult for me right now. The project itself is easy, but
until now I have only done procedural programming, so this is the first time
I am using OOP for real, and it is a big change in thinking.

To be honest, only about **25%** of the code today was written by me. For the
other **75%** I watched the solution and then wrote it in code form, with a
little improvisation of my own. I am not fully convinced by myself about
this. I am a little sad because the project was easy, but as a first time I
am happy with myself.

## Key Takeaway
`__init__` and `self` are the heart of a class. This is my first day with
OOP, so it is normal that it feels hard. The next improvement is to write
more of the code myself and rebuild a class from scratch without watching
the solution. I think I will get better gradually.