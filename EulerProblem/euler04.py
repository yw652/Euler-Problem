import numpy as np
'''
Find the largest palindromic number consists of 2 3-digit number
'''

def palindrome():
    list = []
    for a in range(100,1000):
        for b in range(100,1000):
            c = a * b
            if (c > 99999):
                m = c / 100000
                n = (c - (m * 100000)) / 10000
                l = (c - (m * 100000 + n * 10000)) / 1000
                p = (c - (m * 100000 + n * 10000 + l * 1000)) / 100
                q = (c - (m * 100000 + n * 10000 + l * 1000 + p * 100)) / 10
                r = (c - (m * 100000 + n * 10000 + l * 1000 + p * 100 + q * 10)) / 1
                if (((m == r) & (n == q) & (l == p))):
                    list.append(c)
            if (c > 9999):
                m = c / 10000
                n = (c - (m * 10000)) / 1000
                l = (c - (m * 10000 + n * 1000)) / 100
                p = (c - (m * 10000 + n * 1000 + l * 100)) / 10
                q = (c - (m * 10000 + n * 1000 + l * 100 + p * 10))
                if (((m == q) & (n == p)) ):
                    list.append(c)
    print max(list)

if __name__ == '__main__':
    palindrome()
