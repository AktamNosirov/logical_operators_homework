def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    return bool(1) if ((c-b)>=0 and (b-a)>=0) else bool(0)
print(main(9,8,11))