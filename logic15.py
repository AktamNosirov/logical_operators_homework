def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1=a%10
    x2=a//10
    x3=a//100
    return bool(1) if (x1+x2+x3)%2==1 else bool(0)
print(main(11))