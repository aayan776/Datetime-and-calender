import datetime
import calendar
date_time = datetime.datetime.now()
print(f"Current datetime is {datetime}")
year = date_time.year
month = date_time.month
day = date_time.day
hour = date_time.hour
minute = date_time.minute
second = date_time.second
print(f"Current year is: {year}")
print(f"Current month is: {month}")
print(f"Current day is: {day}")
print(f"Current hour is: {hour}")
print(f"Current minute is: {minute}")
print(f"Current second is: {second}")
month_calender = calendar.month(year, month)
print(f"\nCalender for: {year} - {month}\n")
print(month_calender)
is_leap = calendar.isleap(year)
print(f"Current year is: {"A leap year" if is_leap else "Not a leap year"}")
leap_years = calendar.leapdays(1, 5000000000)
print(f"Leap days in the 21st century: {leap_years}")
specific_date = datetime.date(9999, 12, 31)
weekday = specific_date.strftime("%A")
print(f"{specific_date} is a {weekday}")
try:
    def planecost(city):
        if city == "dhaka":
            return 4000
        elif city == "khulna":
            return 5500
        elif city == "mymensingh":
            return 3000
    def hotelcost(nights):
        return nights * 1000
    def carcost(days):
        return days * 200
    travel_city = input("Enter city you are travelling to: ").lower()
    nights_spent = int(input("Enter amount of nights spent: "))
    days_travelled = int(input("Enter amount of days to rent a car for: "))
    city_travelled = planecost(travel_city)
    hotel_cost = hotelcost(nights_spent)
    car_cost = carcost(days_travelled)
    result = city_travelled + hotel_cost + car_cost
    print(f"Total expenses: {result}")
    str = str(result)
    print(len(str))
except ValueError:
    print("Value error detected")
