 Smallest multiple

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def f(n):
    x = n + 1
    for i in range(2, n + 1):
        if x % i != 0:
           f(n + 1) 
        else:
            return x
         

print(f(10))


