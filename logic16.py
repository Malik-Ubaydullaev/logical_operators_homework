def main(a):
    num1 = pow(0, a)
    a //= 10
    
    num2 = pow(0, a)
    a //= 10
    
    num3 = pow(0, a)
    a //= 10
    
    num4 = pow(0, a)
    a //= 10
    
    num5 = pow(0, a)
    a //= 10
    
    num6 = pow(0, a)
    
    result = num1 == 0 and num2 == 0 and num3 == 0 and num4 == 0 and num5 == 0 and num6 != 0
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a: int
    Returns:
        True if a is five-digit number, False otherwise
    """
    return result