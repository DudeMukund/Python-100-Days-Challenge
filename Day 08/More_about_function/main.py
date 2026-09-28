

#function tht allows for inputs :
def greet(name="dude"):
    print(f"hello {name}!")
    print("how are you")
    print("it's been long to time see you")

greet("Mukund")
greet()

def my_function(somethhing): # here it's parameter
    pass
my_function(123)  # here it's argumnet
# soemthing (parameter) = 123 (argumnet)
#so parametr is name of data we are passing and argumnet is actual value of the data


# functiobn with more than 1 input
def greet_with(name, location):
    print(f"helo {name}")
    print(f"how's wheather in {location} ")

#give argumnet in parameter sequence :postional argumnet
greet_with("dude","india")

#we can do this : keyword arguments
greet_with(location = "india", name="dude")