def main(a,b):
    c = a % 2 != 0 or b % 2 != 0
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is odd".
    Args:
        a: int
        b: int
    Returns:
        True if at least one of the numbers 'a' and 'b' is odd, False otherwise
    """
    return c