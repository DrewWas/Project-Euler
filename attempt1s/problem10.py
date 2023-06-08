# Summation of Primes

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes below 2 million
"""

# To improve this one, maybe write it in C tonight 

def f(x):
    n = 3
    summation = 2
    while n < x:
        isPrime = True
        for i in range(2, int(n ** (1/2)) + 1):
            if n % i == 0:
                isPrime = False

        if isPrime:
            summation += n
        
        n += 1

    return summation


print(f(2000000))




