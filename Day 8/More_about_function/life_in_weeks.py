
def life_in_weks(age):
    '''show how many wekks you left if you live 90 years'''
    remaning_age = 90 - age
    remaning_weeks = remaning_age * 52
    return (f"you have {remaning_weeks} weeks left")
    
age = int(input("Enter your age! "))
print(life_in_weks(age))