def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    return bool(1) if 10<=x<=99 and x==x%10*10+x//10 or 100<=x<=999 and x==x%10*100+x%100//10*10+x//100 else bool(0)
print(main(444))

