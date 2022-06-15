
def leapyear(year):
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        return "This is a leap year"
    else:
        return "This is not a leap year"

year = int(input("Enter a year : "))
leap = leapyear(year)
print(leap)