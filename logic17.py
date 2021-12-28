def main(a):
    num1 = a % 10
    a //= 10
    
    num2 = a % 10
    a //= 10
    
    num3 = a % 10
    a //= 10
    
    num4 = a % 10
    a //= 10
    
    num5 = a % 10
    
    result = num5 > num4 and num4 > num3 and num3 > num2 and num2 > num1
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a: int
    Returns:
        True if all digits of a are in ascending order, False otherwise
    """
    return result