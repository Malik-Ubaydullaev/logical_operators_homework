def main(a):
    num1 = a % 10
    a = a // 10
    
    num2 = a % 10
    a = a // 10
    
    num3 = a % 10
    
    result = (num1 + num2 + num3) % 2 != 0
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a: int
    Returns:
        True if all digits sum is odd, False otherwise
    """
    return result