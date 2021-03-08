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
    
    numbertoConvert = num_str
    isNegative = False
    isHex = False
    isDecimal = False
    output = 0

    if numbertoConvert[0] == "-":
        isNegative = True
        numbertoConvert = numbertoConvert[1:]
    if numbertoConvert[0:2] == "0x":
        isHex = True
        numbertoConvert = numbertoConvert[2:]
    if "." in num_str:
        isDecimal = True

    if not isHex:
        if any(i.isalpha() for i in num_str):
            return None
        output = numberStringtoInt(numbertoConvert, isDecimal)
    if isHex:
        output = hexStringtoInt(numbertoConvert)

    if isNegative:
        output *= -1
    return output


def numberStringtoInt(string, isDecimal):
    output = 0
    stringtoConvert = string
    stringLength = len(string) - 1

    if isDecimal:
        toAdd, decimalIndex = decStringtoInt(string, isDecimal)
        if toAdd == None:
            return None
        output += toAdd
        if decimalIndex == 0:
            return output
        stringtoConvert = string[0:decimalIndex]
        stringLength = len(stringtoConvert) - 1

    for number in stringtoConvert:
        output += hexHash[number] * (10**stringLength)
        stringLength -= 1

    return output


def decStringtoInt(string, isDecimal):

    decimalIndex = string.index(".")
    decString = string[decimalIndex:]
    decLength = len(decString) - 1
    output = 0

    for number in decString[1:]:
        if number == "." and isDecimal:
            return None, decimalIndex
        output += hexHash[number] * (10**decLength)
        decLength -= 1

    output = output / (10**len(decString))
    return output, decimalIndex


def hexStringtoInt(string):

    output = 0
    stringLength = len(string) - 1

    for hexNumber in string:
        if hexNumber.upper() not in hexHash.keys():
            return None
        if hexNumber.isalpha():
            output += hexHash[hexNumber.upper()] * (16 ** stringLength)
            stringLength -= 1
            continue
        output += hexHash[hexNumber.upper()] * (16 ** stringLength)
        stringLength -= 1

    return output
<<<<<<< HEAD

=======
>>>>>>> function1-add-decimal-integer-hex-logic-and-tests
