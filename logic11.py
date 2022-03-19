def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return bool(1) if a>100 and a<1000 else bool(0)
print(main(11185))