def is_leap(year):
    # Check if year is divisible by 400 (leap year)
    if year % 400 == 0:
        return True
    # Check if year is divisible by 100 but not 400 (not a leap year)
    elif year % 100 == 0:
        return False
    # Check if year is divisible by 4 (leap year)
    elif year % 4 == 0:
        return True
    # Otherwise, it's not a leap year
    else:
        return False
  


