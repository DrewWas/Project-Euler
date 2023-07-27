# Sum Square Difference 

"""
The sum of the squares of the first ten natural numbers is 385 

The square of the sum of the first ten natural numbers is 3025

Hence, the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum
"""


def f(x):
    sum_square = sum([i ** 2 for i in range(1, x + 1)])

    square_sum = sum([i for i in range(1, x + 1)]) ** 2

    return square_sum - sum_square


print(f(100))



