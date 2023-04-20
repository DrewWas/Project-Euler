# Largest prime factor 

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(n):
    if not isinstance(n, int):
        return False 
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
            
l = []
def f(n):
    i = 3
    t = yield_primes()

    if 1 in l:
        return max(set(l))

    while n % i != 0:
        i = next(t)    

    l.append(i)
    if is_prime(int(n/i)):
        l.append(int(n / i))
    return f(int(n/i))
         

print(f(600851475143))
