def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return bool(1) if a%11==0 and a>10 and a<100 else bool(0)
print(main(5555))