#Write a program that determines whether a year entered by the user is a leap year or not using if-elif-else statements.
"""
year%4==0&
year%100!=0/
year%400==0https://replit.com/@VelmuruganDhanu/Challenge-12?mobileWebview=1&mobileBridge=1&hideBottomBar=1&forceTheme=replitLight&fun=1#main.py
"""


def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter a year: "))

if isLeapYear(year):  # Call the function and pass the 'year' variable
  print('{} is a leap year.'.format(year))
else:
  print(
      '{} is not a leap year.'.format(year)
  )  # Implement a recursive function to calculate the factorial of a given number.
