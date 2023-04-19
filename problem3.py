# Largest prime factor 

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(n):
    n = int(n)
    for i in range(2, (n // 2) + 1):
        if (n / i).is_integer():
            return False
    return True

def yield_primes():
    n = 2
    while True:
        yield n
        n += 1
        while not is_prime(n):
            n += 1
            
    
   

def f(n):
    l = []
    i = 3
    while len(l) < 3:
        if is_prime(n / i):
            l.append(i)
            l.append(int(n / i))
        else:
            i = next(prime)
         

    return l


print(f(13195))
