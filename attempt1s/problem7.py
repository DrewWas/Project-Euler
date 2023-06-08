# 10001st Prime

"""
By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""


# This one obviously has a iterative and recursive solution, lets see which is
# faster 

# This question is literally just write a prime numbers generator 


# Iterative 
def f(x):
    q = 3
    z = 2
    while z <= x:
        isPrime = True
        for i in range(2, int(q ** (1/2) + 1)):
            if q % i == 0:
                isPrime = False
        if isPrime:
           print("The " + str(z) + " Prime is " + str(q))
           z += 1

        q += 1

    return q
    

print(f(10001))






