def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return bool(1) if a//10>=1 and a//100==0 else bool(0)
print(main(111))