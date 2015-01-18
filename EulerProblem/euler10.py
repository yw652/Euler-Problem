__author__ = 'yitongwang'

'''
Takeaway: When checking whether a number n is prime, check every number in range(2,math.sqrt(n)+1):
if n % i in range(2,math.sqrt(n)+1) != 0, then it is prime
'''

import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def findSum():
    sum = 0
    for i in range(2,2000000):
        if isPrime(i):
            sum += i
    return sum

if __name__ == "__main__":
    print findSum()
