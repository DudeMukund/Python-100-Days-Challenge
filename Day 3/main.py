

print("Welcome to the rollercoaster! ")
height=int(input("Enter your Height in cm? "))

if height > 120:
    print("you can ride rollercoaster!")
else:
    print("sorry yo have to grow taller")

#comparison operators:
##>,<,=<,>=,==(euqal), !=(not equal)
# so a = 2 means i'm assigning 2 into variable a 
# but a==2 now i'm saying value of a is equal to 2


#nested if / else:
#elif will run when it's privous code will fail then elif will run
#and sequence of writing this conitionis : if ->elif->else
print("Welcome to the rollercoaster! ")
height=int(input("Enter your Height in cm? "))
age = int(input("what's your age?" ))

if height > 120:
    if age > 18:
        print("you have to pay $15")
    elif age > 12:
        print("you have to pay $7")
    else:
        print("you have to pay $5")
else:
    print("sorry you have to grow taller")



# you can combine multiple codition by and , or

