def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Argsgi:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1=a%10
    x2=a%100//10
    x3=a%1000//100
    x4=a%10000//1000
    x5=a//10000
    return bool(1) if x1<x2<x3<x4<x5 else bool(0)
print(main(54341))