def main(a):
    num1 = pow(0, a)
    a //= 10
    num2 = pow(0, a)
    a //= 10
    num3 = pow(0, a)
    
    c = num1 == 0 and num2 == 0 and num3 != 0
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a: int
    Returns:
        True if a is two-digit number, False otherwise
    """
    return c