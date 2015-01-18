import numpy as np
import math

def smallMultiple():
    prime = [2,3,5,7,11,13,17,19]
    sum = 1
    #Add exponential to the prime list so that the highest exponential can be from 1-20
    for i in range(0,len(prime)):
        j = 0

        while(math.pow(prime[i],j) < 20):
            j += 1

        prime[i] = math.pow(prime[i],j-1)
    for i in prime:
        sum = sum * i
    return sum

if __name__ == "__main__":
    print int(smallMultiple())





