#event listner

import turtle as t
tim = t.Turtle()
sc = t.Screen()



def move_forward():
    tim.forward(10)

sc.listen() #now screen is able to listen you like he can take input and do some action
sc.onkey(key="space",fun=move_forward) # here i'm saying if i click space bar run move_forward() function



sc.exitonclick()



## high order function : a function work with other function.

# def add(a,b):
#     print( a+b)


# def addition(a,b,fun):
#     fun(a,b)

# adding_two_number = addition
# adding_two_number(6,7,add) #13