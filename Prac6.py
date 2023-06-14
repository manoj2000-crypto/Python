# Write a Python program to find the difference between current date and given date.
from datetime import datetime

str_date1 = input("Enter given date :- ")
str_date2 = input("Enter current date :- ")

date1 = datetime.strptime(str_date1, "%Y/%m/%d")
date2 = datetime.strptime(str_date2, "%Y/%m/%d")

delta = date2 - date1
print("The difference between current date and given date is :- ", delta.days, "days")
