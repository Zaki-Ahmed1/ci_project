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
    """This function takes in a string and converts it into a base 10 number
    and returns it.

    Args:
        num_str (string): returns a base 10 int
    """
    if any(i == " " for i in num_str) or not num_str:
        return None

    # logic parameters handle if the number is negative, a hex, or a decimal
    numbertoConvert = num_str
    isNegative = False
    isHex = False
    isDecimal = False
    output = 0

    # strips the string to a "raw" version and adjusts logic parameters
    if numbertoConvert[0] == "-":
        isNegative = True
        numbertoConvert = numbertoConvert[1:]
    if numbertoConvert[0:2] == "0x":
        isHex = True
        numbertoConvert = numbertoConvert[2:]
    if "." in num_str:
        isDecimal = True

    if not isHex:
        # checks if the string contains any alphabetical numbers\
        # after being designated a non hex string
        if any(i.isalpha() for i in num_str):
            return None
        # calls string integer helper function
        output = numberStringtoInt(numbertoConvert, isDecimal)
    if isHex:
        # calls hex integer helper function
        output = hexStringtoInt(numbertoConvert)

    # makes the output
    # negative if it was designated a "negative" string
    if isNegative:
        output *= -1
    return output


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
