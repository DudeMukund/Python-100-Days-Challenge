
# so if you want to aceess every element and want to print each item so  you have to use For loop
fruits = ["Apple", "Peach","pear"]
#use like this
for fruit in fruits:
    print(fruit)


student_score = [56,35,36,33,90,56,60,89,79,69,57,40,39,190]
print(sum(student_score))
print(max(student_score))
print(min(student_score))


#sum
sum =0 
for i in student_score:
    sum += i
print(sum)

#maximum
max = 0
for i in student_score:
    if i>max:
        max=i
print(f"max is {max}")


#minumun
min = 0
for i in student_score:
    if i<min:
        min =i
print(min)


#range function:
##range(a: start, b-1: end , steps)
###range(1,5)-->1,2,3,4
####range(1,5,2) -->1 , 3
l =[]
for i in range(1,5):
    l.append(i)
print(l)

