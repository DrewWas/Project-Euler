# Power Digit Sum

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of hte number 2^1000
"""

# 2^1000 = (2^500)^2

def square(x):
    return x * x


def f(base, exp):
    if exp == 1:
        return base
    elif exp % 2 == 0:
        return square(f(base, exp // 2))
    else:
        return base * square(f(base, ((exp - 1) // 2)))


def getSum():
    lst = []
    for i in str(f(2, 1000)):
        lst.append((int(i)))
    return sum(lst)


print(getSum())

