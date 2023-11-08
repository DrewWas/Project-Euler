# Factorial Digit Sum

"""
n! means n * (n-1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800
and the sum of the digits of the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0

Find the sum of the digits in the number 100!
"""

def f(n):
    # is there a faster recursion algorithm?
    if n == 1:
        return 1
    else:
        return n * f(n - 1)
    

def getSum():
    lst = []
    for i in str(f(100)):
        lst.append(int(i))
    return sum(lst)


print(getSum())

