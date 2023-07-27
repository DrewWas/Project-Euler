#Longest Collatz Sequence 

"""
The following iterative sequence is defined for the set of positive integers

n --> n / 2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence

13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10
terms. Although it has not been proved yet, it is thought that all starting numbers
finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# Ok so my thinking for this is basically just find the largest odd number, n, under one
# million such that 3n + 1 applied recursively remains odd to the furthest extent


mil = 1000000

n = 0

def f(x):
    return (3 *  x) + 1



def g(f):
    n = 0
    if (f(mil) % 2 == 0:
        return n
    else:
        n += 1
        g(f(f(mil)))


print(g(f(mil)))



