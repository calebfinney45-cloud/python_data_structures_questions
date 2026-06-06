# Write a Python program that counts the number of leap years within the range of years. 
# Ranges of years should be accepted as strings.

def count_leap_years(year_range):
     # split the string and convert to integer
     start_year, end_year = map(int, year_range.split("-"))

     leap_years = 0
     
     # loop through each year in given range inclusive of end year
     for year in range(start_year, end_year + 1):
          # check standard and century leap year rules
          if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
               leap_years += 1
     return leap_years

user_input = input("Enter the year range in the format YYYY-YYYY: ")
print(f"There are {count_leap_years(user_input)} leap years in the range {user_input}")