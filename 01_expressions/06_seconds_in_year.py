# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.
# Constants that help us do the math clearly and easily
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Multiply all values to find out how many seconds are in one year
    print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN) + " seconds in a year!")

# This part runs the main function when the program starts
if __name__ == '__main__':
    main()
