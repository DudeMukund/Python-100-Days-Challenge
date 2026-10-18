# let's study Inhertiance

class Animal:
    def __init__(self):
        self.eye=2
        self.ear=2
    def breathe(self):
        print("Inhale, Exhale")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.leg = 4

    def sass_lena(self):
        super().breathe()
        self.breathe()
        print("i'm taking oxygen and releasing carbodioxide")

    def move(self):
        print("i'm walking!...")

tim = Dog()
print(tim.leg)
tim.move()

tim.breathe()
print(tim.eye)
print(tim.ear)
tim.sass_lena()

# so here you can see we are able to use Animal methods and atrribute in Dog class so this is called Inhertinace.