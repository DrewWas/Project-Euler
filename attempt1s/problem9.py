# Special Pythagorean Triplet

"""
A Pythagorean Triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product of abc
"""

def f():
    from math import sqrt
    a = 0
    b = a + 1
    c = 1000 - (a + b)


    while a**2 + b**2 != c**2:
        print(a,b,c)
        b += 1
        c -= 1
        if c == b or b > c:
            a += 1
            b = a + 1 
            c = 1000 - (a + b)

    prod = a * b * c
    print("final: %s %s %s" % (a,b,c))
    print("product of a*b*c = %s" % (prod))
f()
    


