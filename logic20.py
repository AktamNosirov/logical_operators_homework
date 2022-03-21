def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    x1=n%10
    x2=n%100//10
    x3=n%1000//100
    x4=n%10000//1000
    x5=n%100000//10000
    x6=n%1000000//100000
    number_of_ones=0 
    number_of_zero=0
    if x1-1==0 and 0<n<100000: number_of_ones+=1
    if x1-1==-1 and 0<n<100000 : number_of_zero+=1 
    if x2-1==0 and 0<n<100000 : number_of_ones+=1
    if x2-1==-1 and 0<n<100000 : number_of_zero+=1 
    if x3-1==0 and 0<n<100000 : number_of_ones+=1
    if x3-1==-1 and 0<n<100000 : number_of_zero+=1 
    if x4-1==0 and 0<n<100000 : number_of_ones+=1
    if x4-1==-1 and 0<n<100000 : number_of_zero+=1 
    if x5-1==0 and 0<n<100000 : number_of_ones+=1
    if x5-1==-1 and 0<n<100000 : number_of_zero+=1 
    if x6-1==0 and 0<n<100000 : number_of_ones+=1
    if x6-1==-1 and 0<n<100000 : number_of_zero+=1 
    if number_of_ones>number_of_zero :return bool(1) 
    if number_of_ones<number_of_zero : return bool(0)
    if number_of_ones==number_of_zero : return bool(0)


print(main(1001))