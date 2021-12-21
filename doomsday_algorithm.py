import math

# Doomsday days of the week each century:
# 0 - Tues
# 100 - Sunday
# 200 - Friday
# 300 - Wed
# ...
# 1900 - Wed
# 2000 - Tues
# 2100 - Sunday
# 2200 - Friday


# Doomsday dates per year: 
# Jan 3rd or 4th
# Feb 28th or 29th
# Mar 14th
# Apr 4th
# May 9th
# Jun 6th
# July 11th
# Aug 8th
# Sept 5th
# Oct 10th
# Nov 7th
# Dec 12th

def user_data():
    date = input("Enter a date to find the corressponding day of the week. \n"
        "Please use the format of DD/MM/YYYY... ")
    calculate_day(date)

def calculate_doomsday(year):
    century = math.floor(year/100)*100
    difference_in_years = int(year - century)
    no_of_leap_years = math.floor(difference_in_years / 4)
    adjustment = difference_in_years + no_of_leap_years

    # Multiples of 7 can be discounted to as days will be the same every week
    if adjustment > 7:
        adjustment = adjustment - (math.floor(adjustment / 7) * 7)

    if century % 400 == 0 or year == 0:
        # Will always fall on a Tuesday with no leap year
        return int(7 + 1 + adjustment)
    elif century % 400 == 100:
        # Will always fall on a Sunday with no leap year
        return int(7 + 6 + adjustment)
    elif century % 400 == 200:
        # Will always fall on a Friday with no leap year
        return int(7 + 4 + adjustment)
    elif century % 400 == 300:
        # Will always fall on a Wednesday with no leap year
        return int(7 + 2 + adjustment)

def calculate_day(date):
    user_day = int(date.split("/")[0])
    user_month = int(date.split("/")[1])
    user_year = int(date.split("/")[2])

    list_of_doomsday_dates = ["03/01","28/02","14/03","04/04","09/05","06/06","11/07","08/08","05/09","10/10","07/11","12/12"]
    list_of_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] * 4

    # Find doomsday date that falls in the same month as user date
    for x in list_of_doomsday_dates:
        if int(x.split("/")[1]) == user_month:
            doomsday_date = int(x.split("/")[0])

    day_of_doomsday = calculate_doomsday(user_year)
    print("Day of doomsday is",day_of_doomsday)
    # Check if user date is a leap year, and if so add an extra day to doomsdays in Jan and Feb
    if (user_month == 1 or user_month == 2) and (user_year % 4 == 0 or user_year == 0):
        doomsday_date += 1
        day_of_doomsday += 1

    gap_to_doomsday = user_day - doomsday_date
    print("Gap to doomsday is",gap_to_doomsday)
    if abs(gap_to_doomsday) > 7:
        day_adjustment = gap_to_doomsday - (math.floor(gap_to_doomsday / 7) * 7)
        day_of_the_week = list_of_days[day_of_doomsday + day_adjustment]
    else:
        day_of_the_week = list_of_days[day_of_doomsday + gap_to_doomsday]
    
    print(date, "was on a", day_of_the_week)

if __name__ == "__main__":
    user_data()
