def main(a):
    num1 = a % 10
    num2 = a // 10
    b = num1 == num2
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a: int
    Returns:
        True if all digits of a are the same, False otherwise
    """
    return b