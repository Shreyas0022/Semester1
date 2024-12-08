
import time
from datetime import datetime


current_datetime = datetime.now()


print("a) Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
print("b) Current Year:", current_datetime.year)
print("c) Month of the year:", current_datetime.strftime("%B"))
print("d) Week number of the year:", current_datetime.strftime("%U"))
print("e) Weekday of the week:", current_datetime.strftime("%A"))
print("f) Day of the year:", current_datetime.strftime("%j"))
print("g) Day of the month:", current_datetime.strftime("%d"))
print("h) Day of the week:", current_datetime.strftime("%w"))
