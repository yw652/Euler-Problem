__author__ = 'yitongwang'
import math
import numpy as np
'''
Find the binary complement of user's choice of integer
'''

def complement():
    n = int(raw_input("Enter your choice of integer for binary's complement calculation"))
    list = []
    
    #Decomposing the number to find its binary expression
    while(n != 0):
        list.append(n % 2)
        n /= 2
    
    list = list[::-1]
    binary = []
    
    #Create its binary complement
    for i in list:
        binary.append(1-i)
        
    #Calculate the arithmetic form of the complement
    sum = 0
    for i in range(0, len(binary)):
        sum += math.pow(2,len(binary)-1-i) * binary[i]
    return int(sum)

if __name__ == '__main__':
    print complement()


