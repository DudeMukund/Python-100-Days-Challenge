#subscripting
print("Hello"[4])#o
print("Hello"[-1])#o

#strings
print("123"+"345") #123345

#integer
print(123+345)#468
print(123_345_678)#123345678

#float
print(3.123)

#Bollean
print(True)
print(False)

# print(len(111122)) #it's gives TypeError

#how to find datatype
print(type("hello"))
print(type(12))
print(type(1.12))
print(type(True))

#converting data type to another data type
print(int("123") + int("456")) # it's not you can convert in anyting like abcd no then it's give error
print(bool("hello")) # it's give true if it's not empty
print(bool(""))#it give false if it's empty
print(float(12))

#using f" string It help to make combination with variable and string
print(f"Number of letter in your name: {len(input("Enter a word! " ))}")

#Operators:
print("My age:" + str(12)) # concatenation
print(123 + 456) # Addition
print(456-123)#Subtraction
print(200/20)# divison
print(200//20) # float divsions
print(200 % 2)# modulo Operator
print(20*2) # multiplication
print(20**2)# square


#Calculate BMI
height = 1.65 
weight = 84
bmi =weight / height**2
print(bmi)
print(round(bmi)) # roundup like 3.3-->3,3.8-->4
print(bmi,2) # round up with 2 decimal placeses acuraccy


