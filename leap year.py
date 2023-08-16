
def it_is_a_leap_year(year):
    year = int(year)
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    
user_input = input("enter the years: ")
years = user_input.split()


for year in years :
    if it_is_a_leap_year(year):
        print(f"{year} it is a leap year")

    else :
        print(f"{year} it is a not leap year")

