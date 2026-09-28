# Built-infunction
## the python iterpeter has a nuber of function and types built into it that are always available. 
### print() , len() , input(), max(), round(), count() , range().....etc

#now how to make own function
def sum(a,b):  #def : define  #sum: function name #(a,b): is parameter or type of input it want
    return a+b   # returning output 
s = sum(5,6) # caling the function then a= 5 , b=6 --> 5+6 then return  11 and s=11
print(s)


#function:A function is a named, reusable block of code that performs a specific task. You write it once and call it many times.

def function_name(parameters):
    # body
    return value      # optional



def add(a, b):
    return a + b

result = add(3, 4)
print(result)    # 7


def greet(name="Guest"):
    print("Hello,", name)

greet()          # Hello, Guest
greet("Amit")    # Hello, Amit


#*args: any number of positional arguments
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))    # 10


#**kwargs: any number of keyword arguments
def show(**data):
    print(data)

show(name="Sam", age=20)    # {'name': 'Sam', 'age': 20}


#Returning multiple values
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([4, 1, 9])



#scope (local or global)
x = 10           # global

def f():
    y = 5        # local, exists only inside f()
    print(x, y)

f()
# print(y)  -> Error, y is not defined outside