import numpy as np
'''
Find the largest prime factor of n
'''


def findFactor():
    n = 2520
    list = []
    d = 2
    while n > 1:
        while n % d == 0:
            list.append(d)
            n = n / d
        d = d + 1
    print max(list)

if __name__ == "__main__":
    findFactor()


