def main(a):
    num1 = pow(0, a)
    a //= 10
    
    num2 = pow(0 ,a)
    a //= 10
    
    num3 = pow(0, a)
    a //= 10
    
    num4 = pow(0, a)
     
    b = num1 == 0 and num2 == 0 and num3 == 0 and num4 != 0
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a: int
    Returns:
        True if a is three-digit number, False otherwise
    """
    return b