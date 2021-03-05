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
    
    # year
    
    # days = num_sec / (24*60*60) # secs/ (secs/day) --> days
    # remainder = num_sec % (24*60*60) # sec remainder --> overflow



    return 0



# Test
print(my_datetime(0))
print(my_datetime(123))