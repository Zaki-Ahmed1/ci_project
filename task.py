# Name: Zaki Ahmed, Bryan Rodriguez, John Tran
# Date: 22 Feb 2021
# Class: CS 362
# Assignment: Group Project: Part 1


hexHash = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


# Function 1
def conv_num(num_str):
    """
    This function takes in a string and converts it into a base 10 number
    and returns it.
    Args: num_str (string): returns a base 10 int
    """

    if not num_str:
        return None

    if stringCleanerHelper(num_str) is None:
        return None

    # logic parameters handle if the number is negative, a hex, or a decimal
    numbertoConvert, isNegative, isHex, isDecimal = stringCleanerHelper(
        num_str)

    if not isHex:
        # checks if the string contains any alphabetical numbers\
        # after being designated a non hex string
        if any(i.isalpha() for i in num_str):
            return None
        # calls string integer helper function
        output = numberStringtoInt(numbertoConvert, isDecimal)
    if isHex:
        # calls hex integer helper function
        # logic below checks that only alphabetical
        # and numeric numbers are left after parsing out
        # hex prefix
        if any(not i.isalpha() and not i.isnumeric()
               for i in numbertoConvert):
            return None
        output = hexStringtoInt(numbertoConvert)

    # makes the output
    # negative if it was designated a "negative" string
    if isNegative:
        output *= -1
    return output


def stringCleanerHelper(string):
    """a helper function to clean the string to be converted
    into an integer

    Args:
        string (str): the string to be cleaned

    Returns:
        None: return None if the string is not a valid input
        string: returns a cleaned version of the string
        isNegative: returns a boolean if the number is negative
        isHex: returns a boolean if the number is a hex number
        isDecimal: return a boolean if the number has a decimal in it
    """

    numbertoConvert = string
    isNegative = False
    isHex = False
    isDecimal = False

    # strips the string to a "raw" version and adjusts logic parameters
    if type(numbertoConvert) is not str:
        return None
    if numbertoConvert[0] == "-":
        isNegative = True
        if len(numbertoConvert) == 1:
            return None
        numbertoConvert = numbertoConvert[1:]
    if numbertoConvert[0:2] == "0x":
        isHex = True
        numbertoConvert = numbertoConvert[2:]
    if "." in numbertoConvert:
        isDecimal = True

    if any(i == " " for i in numbertoConvert) or not numbertoConvert:
        return None

    return (numbertoConvert, isNegative, isHex, isDecimal)


def numberStringtoInt(string, isDecimal):
    """a helper function that takes in a "cleaned"
    string and converts the string to an integer.
    The "cleaned" string comes form conv_num()

    Args:
        string (str): the string to be created into an integer
        isDecimal (bool): True if the number contains a decimal,
        used for the decimal integer helper function

    Returns:
        int: the int representation of the string passed to the function
    """
    output = 0
    stringtoConvert = string
    stringLength = len(string) - 1

    # if the string is a decimal number,
    # the number is passed into the decimal string helper
    if isDecimal:
        toAdd, decimalIndex = decStringtoInt(string, isDecimal)
        # logic returns none if there is more than one decimal passed
        if toAdd is None:
            return None
        output += toAdd
        if decimalIndex == 0:
            return output
        # removes the string portion after
        # the decimal on the number to be converted to an int
        stringtoConvert = string[0:decimalIndex]
        stringLength = len(stringtoConvert) - 1

    # converts the string numbers to integers
    for number in stringtoConvert:
        if not number.isnumeric():
            return None
        output += hexHash[number] * (10**stringLength)
        stringLength -= 1

    return output


def decStringtoInt(string, isDecimal):
    """a helper function that takes in a "cleaned" decimal
    string and converts the string to an integer.
    The "cleaned" string comes form decStringtoInt

    Args:
        string (string): the decimal portion of the
        string to create into an integer
        isDecimal (bool): a boolean denoting the
        string a decimal, used for logic check

    Returns:
        integer: the decimal int representation of
        the string passed to the function
    """
    decimalIndex = string.index(".")
    decString = string[decimalIndex:]
    decLength = len(decString) - 1
    output = 0

    # converts the string decimal to an integer
    for number in decString[1:]:
        # checks for multiple decimals passed in the string
        if number == "." and isDecimal:
            return None, decimalIndex
        output += hexHash[number] * (10**decLength)
        decLength -= 1

    # divide the output to create the decimal
    output = output / (10**len(decString))
    return output, decimalIndex


def hexStringtoInt(string):
    """a helper function that takes in a "cleaned"
    hex string and converts it to an integer
    The "cleaned string comes from conv_num()

    Args:
        string (string): the hex portion of the string to
        be created into an integer

    Returns:
        int: the hex respresentation of the
        string passed to the function
    """

    output = 0
    stringLength = len(string) - 1

    # converts the string hex to an integer
    for hexNumber in string:
        # checks if letters have been that are not part of the hexHash table
        if hexNumber.upper() not in hexHash.keys():
            return None
        if hexNumber.isalpha():
            # converts lower case hex values to uppercase
            output += hexHash[hexNumber.upper()] * (16 ** stringLength)
            stringLength -= 1
            continue
        output += hexHash[hexNumber] * (16 ** stringLength)
        stringLength -= 1

    return output


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

    if num_sec > (86400 * 365 * 8035 + 86400 * 122):
        return "12-31-9999"

    # Calculate how many num_days needed to iterate...
    num_days = num_sec / (24 * 60 * 60)
    remainder = num_sec % (24 * 60 * 60) / (24 * 60 * 60)
    num_days = num_days - remainder

    # Initialize values for counting...
    count_day = 0

    # Iterate through each year up to max range...
    for year in range(0, 9999):

        # Set flag and break loop if...
        level_1 = False

        if count_day >= num_days:
            level_1 = True
            break

        actual_year = 1970 + year
        count_month = 0

        if is_leap_year(actual_year):
            for month in calendar_leap:

                # Set flag and break loop if...
                level_2 = False

                if count_day >= num_days:
                    level_2 = True
                    break

                count_month += 1
                day, count_day, level_3 = day_looper(month, count_month,
                                                     count_day, num_days)

        else:
            for month in calendar:

                # Set flag and break loop if...
                level_2 = False

                if count_day >= num_days:
                    level_2 = True
                    break

                count_month += 1
                day, count_day, level_3 = day_looper(month, count_month,
                                                     count_day, num_days)

    # Adjust date / year if necessary on special cases...
    day, count_month, actual_year = day_adjustor(level_1, level_2, level_3,
                                                 day, count_month, actual_year)

    # Build string for output...
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
    Parameters: Month (int), Count of Month (int), Count of Days (int),
                Number of Days (int)
    Returns: Day of Month (int), Count of Days (int)
    Summary: Iterates through the number of days in each month
    """

    # Iterate through the days in each month whilst keeping count...
    for day in range(mon[0], mon[1] + 1):

        # Set flag and break loop if...
        level_3 = False

        if count_da >= num_da:
            level_3 = True
            break

        count_da += 1

    return day, count_da, level_3


def day_adjustor(level_1, level_2, level_3, day, count_month, actual_year):
    """
    Parameters: Level 1 (bool), Level 2 (bool), Level 3 (bool)
                Day (int), Count of Month (int), Year (int)
    Returns: Day of Month (int), Count of Month (int), Year (int)
    Summary: Adjusts the date if the loop has ended on a 31st or end of year.
    """

    # Adjustment for when break occurs on 31st of the month...
    if level_1 is True and level_2 is True and level_3 is False:
        day = 1
        count_month += 1

    # Adjustment for when break occurs on 31st of last lonth of year...
    if level_1 is True and level_2 is False and level_3 is False:
        day = 1
        count_month = 1
        actual_year += 1

    # Adjusting display for reaching limits of function...
    if actual_year > 9999:
        day = 31
        count_month = 12
        actual_year = 9999

    return day, count_month, actual_year


# Function 3
def conv_endian(num, endian='big'):
    val_num = num
    num = abs(num)
    array = []
    # Check num
    if num == 0:
        return "00"
    # Check if parameter endian is big and little
    if endian != "big" and endian != "little":
        return None
    while num != 0:
        # Append value of value
        remainder = num % 16
        num = int(num / 16)
        if remainder > 9:
            val = chr(ord('A') + remainder - 10)
            array.append(val)
        else:
            # Append value of remainder
            array.append(remainder)
    # If length of array is odd, append 0
    if len(array) % 2 == 1:
        array.append(0)

    ans = ""
    temp = ""
    for i in range(len(array) - 1, -1, -1):
        temp = temp + str(array[i])
        ans, temp = conv_endian_help(i, endian, temp, ans)

    if endian == 'little':
        # remove space when adding negative
        ans = ans[:-1]
        # reverse the array (doing a second reverse here)
        ans = ans[::-1]
    # if number less than 0 (which is negative) add symbol
    if val_num < 0:
        ans = "-" + ans
    # remove the last space at the end
    if ans[len(ans) - 1] == " ":
        ans = ans[:len(ans) - 1]
    return ans


def conv_endian_help(i, endian, temp, ans):
    if i % 2 == 0:
        if endian == 'little':
            temp = temp[::-1]
        ans = ans + temp
        ans = ans + " "
        temp = ""

    return ans, temp
