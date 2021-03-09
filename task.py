

# Specify num_days for normal calendar year...
calendar = [
    [1, 31],    # Jan
    [1, 28],    # Feb
    [1, 31],    # Mar
    [1, 30],    # Apr
    [1, 31],    # May
    [1, 30],    # Jun
    [1, 31],    # Jul
    [1, 31],    # Aug
    [1, 30],    # Sep
    [1, 31],    # Oct
    [1, 30],    # Nov
    [1, 31]     # Dec
]

# Specify num_days for lear calendar year...
calendar_leap = [
    [1, 31],    # Jan
    [1, 29],    # Feb (leap)
    [1, 31],    # Mar
    [1, 30],    # Apr
    [1, 31],    # May
    [1, 30],    # Jun
    [1, 31],    # Jul
    [1, 31],    # Aug
    [1, 30],    # Sep
    [1, 31],    # Oct
    [1, 30],    # Nov
    [1, 31]     # Dec
]


# Function 2
def my_datetime(num_sec):
    """
    Parameters: Seconds (int)
    Returns: Date (str) --> MM-DD-YYYY
    Summary: Converts number of seconds to date stamp since Epoch time.
    """

    # Initial input handling...
    if num_sec < (24 * 60 * 60):
        return "01-01-1970"

    # Calculate how many num_days needed to iterate...
    num_days = num_sec / (24 * 60 * 60)
    remainder = num_sec % (24 * 60 * 60) / (24 * 60 * 60)
    num_days = num_days - remainder

    # Initialize values for counting...
    count_day = 0


    # Iterate through each year up to max range...
    for year in range(0, 9999):

        # Break loop if...
        level_1 = False
        if count_day >= num_days:
            level_1 = True
            print("Level 1")
            break

        actual_year = 1970 + year
        count_month = 0


        if is_leap_year(actual_year):
            for month in calendar_leap:
                level_2 = False
                if count_day >= num_days:
                    level_2 = True
                    print("Level 2")
                    break

                count_month += 1
                day, count_day, level_3 = day_looper(month,
                                            count_month, count_day, num_days)

        else:
            for month in calendar:
                level_2 = False
                if count_day >= num_days:
                    level_2 = True
                    print("Level 2")
                    break

                count_month += 1
                day, count_day, level_3 = day_looper(month,
                                            count_month, count_day, num_days)

    day, count_month, actual_year = day_adjustor(level_1, level_2, level_3, day, count_month, actual_year)
    # if level_1 == True and level_2 == True and level_3 == False:
    #     day = 1
    #     count_month += 1
    # if level_1 == True and level_2 == False and level_3 == False:
    #     day = 1
    #     count_month = 1
    #     actual_year += 1

    string = str(count_month).zfill(2) + "-" + str(day).zfill(2)
    string += "-" + str(actual_year)
    return string


def is_leap_year(year):
    """
    Parameters: Year (int)
    Returns: Boolean (bool)
    Summary: Verifies if a given year is a leap year.
    """

    return (year % 4 == 0 and (
        (year % 100 == 0 and year % 400 == 0) or year % 100 != 0))


def day_looper(mon, count_month, count_da, num_da):
    """
    Parameters: Month (int), Count of Days (int), Number of Days (int)
    Returns: Day of Month (int), Count of Days (int)
    Summary: Iterates through the number of days in each month
    """

    # Iterate through the days in each month whilst keeping count...
    for day in range(mon[0], mon[1] + 1):
        # count_da += 1
        level_3 = False
        if count_da >= num_da:
            level_3 = True
            print("Level 3")
            break
        count_da += 1

    return day, count_da, level_3

def day_adjustor(level_1, level_2, level_3, day, count_month, actual_year):
    if level_1 == True and level_2 == True and level_3 == False:
        day = 1
        count_month += 1
    if level_1 == True and level_2 == False and level_3 == False:
        day = 1
        count_month = 1
        actual_year += 1
    if actual_year > 9999:
        day = 31
        count_month = 12
        actual_year = 9999
    return day, count_month, actual_year

# print("Day 1 close to midnight")
# print(my_datetime(86398))
# print(my_datetime(86399))
# print(my_datetime(86400), "Midnight") #midnight
# print(my_datetime(86401))
# print(my_datetime(86402))
# print()
# print("Day 2 close to midnight")
# print(my_datetime((86400*2)-2))
# print(my_datetime((86400*2)-1))
# print(my_datetime(86400*2), "Midnight") # midnight
# print(my_datetime((86400*2)+1))
# print(my_datetime((86400*2)+2))
# print()
# print("Day 3 close to midnight")
# print(my_datetime((86400*3)-2))
# print(my_datetime((86400*3)-1))
# print(my_datetime(86400*3), "Midnight") # midnight
# print(my_datetime((86400*3)+1))
# print(my_datetime((86400*3)+2))
# print()
# print(my_datetime(86400*29))
# print(my_datetime(86400*30))
# print(my_datetime(86400*31))
# print(my_datetime(86400*32))
# print()
# print(my_datetime(86400*363))
# print(my_datetime(86400*364))
# print(my_datetime(86400*365))
# print(my_datetime(86400*366))
# print(my_datetime(86400*367))
# print()
# print(my_datetime(86400*363*5))
# print(my_datetime(86400*364*5))
# print(my_datetime(86400*365*5))
# print(my_datetime(86400*366*5))
# print(my_datetime(86400*367*5))
# print()



# END Testing
# for num in range(2932100+365*2, 2933105):
#     print("For the", str(num).zfill(2), "th day...the date is:", my_datetime(86400 * num))


for num in range(2*350, 2*375):
    print("For the", str(num).zfill(2), "th date...the date is:", my_datetime(86400 * num))
