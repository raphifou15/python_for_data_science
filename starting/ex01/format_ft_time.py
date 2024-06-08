import time
import datetime
import calendar

seconds = time.time()
science = "{:.2e}".format(seconds)
secondesFr = f"{seconds:,.4f}"
str = f"Seconds since January 1, 1970: {secondesFr} or {science} in scientific notation"

date_time = datetime.datetime.fromtimestamp(seconds)
month_number = date_time.month
day_number = date_time.day
year_number = date_time.year
month_name = calendar.month_name[month_number]
str2 = f"{month_name} {day_number} {year_number}"

print(str)
print(str2)


# print(time.ctime(seconds))