# Longest Collatz Sequence

"""
The following iterative sequence is defined for the set of positive integers:
n __> n/2 (n is even)
n --> 3n + 1 (n is odd) 

Using the rule above and starting with 13, we generate the followin sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proven yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under 1 million, produces the longest chain?
"""


mapping = {}


def collatz(n):
    length = 0 
    while n != 1:
        if n % 2 == 0:
            n = n // 2 
            if n in mapping.keys():
                length += mapping[n]
                return length
        else:
            n = (3*n) + 1
            if n in mapping.keys():
                length += mapping[n]
                return length
        length += 1
    return length



def f(x):
    # x = 1 million
    for i in range(1, x + 1):
        n = i
        mapping[i] = None
        key = collatz(i)
        mapping[i] = key

    return "starting number: " + str(max(mapping, key=mapping.get)), "steps: " + str(max(mapping.values()))


print(f(1000000))




