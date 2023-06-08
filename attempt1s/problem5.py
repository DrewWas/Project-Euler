#Smallest multiple

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# There is def a recursive solution for this 
# Maybe in my next attempt I'll try it 

# ^^ Actually probably not because recursion can't go as deep as it would need to for
# this 

def f(n):
    x = n + 1
    while not (x % 10 == 0 and x % 9 == 0 and x % 8 == 0 and x % 7 == 0 and x % 6 == 0):
        x += 1

    return x



def g(n):
    x = n + 1

    while not (x % 20 == 0 and x % 19 == 0 and x % 18 == 0 and x % 17 == 0 and x % 16 ==
0 and x % 15 == 0 and x % 14 == 0 and x % 13 == 0 and x % 12 == 0 and x % 11 == 0):
        x += 1

    return x
    
print(g(20))

# This would be a lot cleaner if we could figure out how to just check divisibility by a range 

# Is there some fundamental math that I'm missing that would make the computation
# quicker??

