# Multiples of 3 or 5

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def f(n):
    l = []
    i = 0
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
        i += 1

    return sum(l)


print(f(1000))
