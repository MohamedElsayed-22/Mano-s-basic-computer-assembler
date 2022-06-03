#function that find the hexadecimal value of the negative decimal values 
def cal_hexa(value):
    """
    This function calulate the complement of the hexadecimal values of negative 
    decimal numbers given in the assembly code
    """
    return hex(2**16 + value)[2:].upper()

def convert_to_decimal(value):
    """
    This function converts the hexadecimal value given in the assembly code 
    and convert it to decimal to do all the math manipulations
    """
    return int(value, 16)
    
    
def convert_to_hexa(value):
    """
    this function converts the decimal number to hexadecimal
    """
    return hex(value)[2:].upper()