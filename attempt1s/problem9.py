# Special Pythagorean Triplet

"""
A Pythagorean Triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product of abc
"""



def f(x):

    while x > 1:
        if (x ** (1/2) % 1) == 0:
            a = x - 1
            b = x - a
            print(x, a, b) 

        x -= 1
        
        


print(f(1000 * 1000))
    



