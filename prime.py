def is_prime(val):
    """
    INPUT: A number
    OUTPUT: prints prime or not
    This function checks for prime numbers
    """
    lst = []
    for num in range(1,val):
        if num <= 1:
            print str(num) + ' is not a prime number'
        elif num == 2:
            print str(num) + ' is prime number'
            lst.append(num)
        else:
            for n in range(2, num):
                if num % n == 0:
                    print '%s is Not a Prime number' %num
                    break
            else:
                print 'The number %s is prime' %num
                lst.append(num)
                
    print lst