import numpy as np
'''
Find the sum of all the even-valued terms in Fibonacci sequence whose value is less than 4 million
'''

def findSum():
    a = 1
    b = 2
    c = a + b
    sum = 2
    while(c < 4000000):
        a = b
        b = c
        c = b + a
        if (c % 2 == 0):
            sum = sum + c
    print sum

if __name__ == '__main__':
    findSum()



