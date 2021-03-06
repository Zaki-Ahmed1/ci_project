# Name: Zaki Ahmed, Bryan Rodriguez, John Tran
# Date: 22 Feb 2021
# Class: CS 362
# Assignment: Group Project: Part 1


# Function 1
# ! cannot use int(), float(), hex(), literal_eval()
def conv_num(num_str):
    """This function takes in a string and converts it into a base 10 number
    and returns it.

    Args:
        num_str (string): returns a base 10 int
    """

    pass


def my_datetime(num_sec):

    if num_sec == 0:
        return "01-01-1970"
    
    year = 1970
    day = 1
    month = 1

    year_count = 0
    month_count = 0
    day_count = 0

    calendar = [
        [1, 31],    # Jan
        [1, 28],    # Feb
        [1, 31],    # Mar
        [1, 30],    # Apr
        [1, 30],    # May
        [1, 31],    # Jun
        [1, 31],    # Jul
        [1, 31],    # Aug
        [1, 30],    # Sep
        [1, 31],    # Oct
        [1, 30],    # Nov
        [1, 31]     # Dec
    ]

    calendar_leap = [
        [1, 31],    # Jan
        [1, 29],    # Feb (leap)
        [1, 31],    # Mar
        [1, 30],    # Apr
        [1, 30],    # May
        [1, 31],    # Jun
        [1, 31],    # Jul
        [1, 31],    # Aug
        [1, 30],    # Sep
        [1, 31],    # Oct
        [1, 30],    # Nov
        [1, 31]     # Dec
    ]
    
    day_increment = 0

    days = num_sec / (24*60*60) # secs/ (secs/day) --> days
    remainder = num_sec % (24*60*60) / 86400 # sec remainder --> overflow
    print("days = ", days)
    print("remainder = ", remainder)
    print()


    for year in range(0, 15):
        
        year_count = year
        actual_year = 1970 + year_count

        print("Year Count = ", year_count)
        print("Actual year = ", actual_year)

        if actual_year % 4 == 0:
            print(actual_year, "is a leap year")
        print("--")



        # for month in calendar:
        #     month_count += 1
        #     for day in range(month[0], month[1]):
    return 0



# Test
print(my_datetime(0))
print()
# print(my_datetime(123))
print(my_datetime(123456789))



