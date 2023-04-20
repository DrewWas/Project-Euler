# Largest palindrome product

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def f(n, i):
    palendrome = n * i 
    while str(palendrome) != str(palendrome)[::-1]:
        for i in range(n, n - 100, -1):
            palendrome = n * i
            print(n, i, palendrome)
            if str(palendrome) == str(palendrome)[::-1]:
                return palendrome


        print("-------------------")
        n -= 1

    return n * i



        
print(f(999,999))


# Bit of a mickey-mouse implementation, but it works *shrug emoji*
