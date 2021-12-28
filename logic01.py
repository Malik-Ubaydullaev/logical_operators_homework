def main(a,b,c):
    d = (a <= b and b <= c) or (a >= b and b >= c )
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a: int
        b: int
        c: int
    Returns:
        True if b is between a and c, False otherwise
    """
    return d