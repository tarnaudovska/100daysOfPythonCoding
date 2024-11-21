def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]

year = int(input("Write the year\n")) # Enter a year
month = int(input("Write the month\n")) # Enter a month

print (f"The {month} month of the {year} year, has {days_in_month(year, month)} days")

if is_leap(year):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")

