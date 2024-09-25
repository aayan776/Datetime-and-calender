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