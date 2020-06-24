def sigma(numinput):
    if numinput <=0:
        return 0
    elif numinput ==1:
        return 1
    else:
        return numinput + sigma(numinput-1)
print(f'sigma of 5: {sigma(5)}')

def factorial_fast(n):
    factorial = 1
    if n >= 1 or n == 0:
        for i in range (1, n +1):
            factorial *= i
            #print("Factorail of ",n , " is : ",factorial)
        return factorial
            
print( factorial_fast(5) )

def factorial_slow(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * factorial_slow(n - 1)
print( factorial_slow(5) )




