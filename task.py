# Name: Zaki Ahmed, Bryan Rodriguez, John Tran
# Date: 22 Feb 2021
# Class: CS 362
# Assignment: Group Project: Part 1

import random

# Function 1
# ! cannot use int(), float(), hex(), literal_eval()


def conv_num(num_str):
    """This function takes in a string and converts it into a base 10 number
    and returns it.

    Args:
        num_str (string): returns a base 10 int
    """

    pass



# Function to calculate the date based on seconds since Epoch
def my_datetime(num_sec):
    """
    Parameters: Seconds(int)
    Returns: Date(str)
    Summary: Converts number of seconds to date stamp since Epoch time (01-01-1970)
    """

    # Initial input handling...
    if num_sec <= 86399:
        return "01-01-1970"

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

    # Calculate how many num_days needed to iterate...
    num_days = num_sec / (24*60*60)
    remainder = num_sec % (24*60*60) / (24*60*60)
    print("Days = ", num_days)  # Print for debugging

    num_days = num_days - remainder
    print(type(num_days))
    print("Days = ", num_days)  # Print for debugging
    print("Remainder = ", remainder)
    print()

    # Initialize values for Epoch year...
    start_year = 1970
    start_day = 1
    start_month = 1

    # Initialize values to start counting...
    count_year = 0
    count_month = 0
    count_day = 0


    # Iterate through each year up to max range...
    for year in range(0, 9999):

        # Break loop if
        if count_day >= num_days:
            # print("Loop broken at year stage", count_day, ">=", num_days)
            break

        count_year = year
        actual_year = 1970 + count_year
        # print()
        # print("Year Count = ", count_year)
        # print("Actual year = ", actual_year)

        count_month = 0

        if actual_year % 4 == 0 and ((actual_year % 100 == 0 and actual_year % 400 == 0) or actual_year % 100 != 0):

            # print(actual_year, " - is a leap year")
            # print()


            for month in calendar_leap:
                if count_day >= num_days:
                    # print("Loop broken at month stage", count_day, ">=", num_days)
                    break

                count_month += 1
                # print("Month currently = ", count_month)


                for day in range(month[0], month[1] + 1):

                    if count_day >= num_days:
                        # print("Loop broken at day stage", count_day, ">=", num_days)
                        break

                    count_day += 1
                    # print("(L)day increased to: ", count_day)
                    # print("X of the month", day)



        else:
            for month in calendar:

                if count_day >= num_days:
                    # print("Loop broken at month stage", count_day, ">=", num_days)
                    break

                count_month += 1
                # print("Month currently = ", count_month)


                for day in range(month[0], month[1] + 1):

                    if count_day >= num_days:
                        # print("Loop broken at day stage", count_day, ">=", num_days)
                        break

                    count_day += 1
                    # print("(N)day increased to: ", count_day)
                    # print(day, "_ of the month")
                    # print("HELLOOOOOOOOOOO WORLD")

    # if remainder > 0:
    #     print("There is a remainder...")
    #     print("The date is...", day)
    #     # count_day += 1
    #     day += 1
    #     print("but with the remainder we have incremented to the next day...", day)

    print(start_month, start_day, start_year)
    print("Days = ", num_days)  # Print for debugging
    print("Remainder = ", remainder)
    print()

    print("Month = ", count_month, "-- Days = ",
          count_day, "-- Year = ", count_year)
    print("Month = ", count_month, "-- Days = ",
          day, "-- Year = ", actual_year)

    print("Final Answer = ", count_month, "/", day, "/", actual_year)

    return 0




# Test
# print(my_datetime(0))
# print()
# print(my_datetime(123))
# print(my_datetime(604800)) #7 num_days
# print(my_datetime(3888000)) # 45 num_days

# print(my_datetime(123456789))
# print(my_datetime(9876543210))
# print(my_datetime(201653971200))


# print(my_datetime(0))
# print()
# print(my_datetime(123))
# print(my_datetime(1200500))
# print(my_datetime(604800)) #7 num_days
# print(my_datetime(3888000)) # 45 num_days

# print(my_datetime(123456789))
# print(my_datetime(9876543210))
# print(my_datetime(201653971200/2/2))

# print(my_datetime(201653971200))

# print(my_datetime(253402243200))

# print(my_datetime(86400*300))


# for num in range(0,1000):
#     my_datetime(num.random.randint())


# print(my_datetime(200632931312))
# print(my_datetime(201653971200))

# 01 / 01 / 5320
# print(my_datetime(105747408000))

# print(my_datetime(86400*365))
# print(my_datetime(86400*366))