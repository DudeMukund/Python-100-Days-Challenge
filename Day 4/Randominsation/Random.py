# Randomisation and Python Lists:
##module: so people spilt codes in module where each module is resposible for  different functionality or purpose and like let's assume you working on a bigger project and you have many many modules so you can collabrate with anyone.

#so see i also created a module and use it 
import my_module 
print(my_module.pie)

#Radominastion
import random # we impoort random module
num = random.randint(1,2) # so it generate a number which is equal to grater and equal to 1 and less and equal than 2
print(num)


#generate random floating no b/w 0 and 1 and not 1
fl=random.random()  # and it doesn;t take input
print(fl)

#genearting Random flating number where numbeer a=< number >= b 
rand_float = random.uniform(1,10)
print(rand_float)



