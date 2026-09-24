#list is data structure like it store multiple type of data like : int,float , ....etc
# Python lists are containers to store a set of values of any data type.
list=["apple",1 , True , 1.5 , "mukund"]
list[0]="orange"
print(list)#['orange', 1, True, 1.5, 'mukund']---> see lists are mutable you can change it


#list are same as string so you can do indexing , slicing..etc


#LIST METHODS:
prl1 = [1,8,7,2,21,15]
print(len(l1)) #6
print(l1[0:4:2])#[1,7]


l1.sort() #updates the list to [1,2,7,8,15,21]
l1.reverse() #updates the list to [15,21,2,7,8,1]
l1.append(8) #adds 8 at the end of the list [21,15,8,7,2,1,8]
l1.insert(3,8) #This will add 8 at 3 index [21,15,8,8,7,2,1,8]
print(l1)
l1.pop(2) #Will delete element at index 2 and return its value.[21,15,8,7,2,1,8]
print(l1)
l1.remove(21) #Will remove 21 from the list.[15,8,7,2,1,8]
print(l1)

l1 = [1,8,7,2,21,15]
print(l1.sort())#none
print(l1)#[1, 2, 7, 8, 15, 21]
print(l1.append(8))#none
print(l1)#[1, 2, 7, 8, 15, 21,8]

l1 = [1,8,7,2,21,15]
print(l1.pop(2))#7
v=l1.pop(1)
print(v)#8
print(l1)#[1, 2, 21, 15]




#SPO THIS IS IMPORTANT FOR ITERATIONS:
a=(1,2)
x,y= a 
print(x,y)



l1=[1,2]
x,y=l1
print(x,y)#1,2










l=[]
L=[]
m=["@","#","$","*"]
l.append(1)
l.append(2)
l.append(3)
print(l)
L.append("a")
L.append("b")
print(L)

x=[]
x.append(l)
x.append(L)
x.append(m)
print(x)#[[1, 2, 3], ['a', 'b'], ['@', '#', '$', '*']]
#list within a list.

z=[]
z.append(x)
print(z)#[[[1, 2, 3], ['a', 'b'], ['@', '#', '$', '*']]]
#list within list within list.

print(z[0][0])#[1, 2, 3] #this is called indexing.
print(z[0][0][0]) #1
#YOU CAN ALSO DO THIS 
m=[]
m.append([1,2,3])
m.append(["a","b","c"])
print(m)#[[1, 2, 3], ['a', 'b', 'c']].
print(m[0])#[1, 2, 3]



#LISTS AND SETS:
l=list(range(11))
print(l)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(5 in l)#true # is 5 is in or not
print(l[-1])#10



l=list(range(1,21))
print(l)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

l=list(range(21))
print(l)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


l=list (range(100000000))# it also take time to create the list because it range is big.
print(-1 in l)# when you run this it take long time give true becuse i itearting to very big range so that's the reason # 4 sec




l=list (range(100000000000000000))
print("s" in l)# if run this code then it say memory error becauuse this is very big range so you can say that a computer is fast but not infinetly fastestfastest.


l="mukund"
print(l)#mukund
del l
print(l)#error

x=[1,2,3,4,5,6,7,8,9,0,1]#list
x.insert(0,0)
x.remove(9)
x.append(10)
print(x)#[0,1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 10]
del x
print(x)#NameError: name 'x' is not defined



#netsed list;
##list under lists
num = [[1,2,3],[4,5,6],[7,8,9]]
print(num[0][1])