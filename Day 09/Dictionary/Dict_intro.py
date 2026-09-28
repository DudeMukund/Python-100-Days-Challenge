#Every  dictionary have key and vallue pair.
#dict = {key : value}
dict1 = {
        "name": "dude",
        "age":20, 
        "language":"python"
        }
print(dict1["name"])  # accesing dictionary elemnt by key

#adding new entery
dict1["major"]="Data sci"
print(dict1)

#edit item in dictionary
dict1["age"] = 21
print(dict1)



# loop in dictionary
for i in dict1:
    print(i)   # it's just give you key
    print(dict1[i]) # printing values 


# excerise: converting score into grades and storing in another empty dictionary
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for i in student_scores:
    if student_scores[i] > 90:
        student_grades[i] = "Outstanding"
    elif student_scores[i] >80:
        student_grades[i] = "Exceeds"
    elif student_scores[i] > 70:
        student_grades[i] = "Acceptable"
    elif student_scores[i] <71:
        student_grades[i] = "Fail"
print(student_grades)
        