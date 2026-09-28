def is_leap_year(year):
    '''it's calculate  year is leap year or not'''  ## this is called docsting when you use inside function
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "It's a leap year"
            else:
                return "It's not a leap year"
        else:
            return "It's a leap year"
    else:
        return "It's not a leap year"
year = int(input("enter a year?  "))
print(is_leap_year(year))