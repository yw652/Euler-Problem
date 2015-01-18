__author__ = 'yitongwang'
import math
import numpy as np


def complement():
    n = int(raw_input())
    list = []
    while(n != 0):
        list.append(n % 2)
        n /= 2
    list = list[::-1]
    binary = []
    for i in list:
        binary.append(1-i)
    sum = 0
    for i in range(0, len(binary)):
        sum += math.pow(2,len(binary)-1-i) * binary[i]
    return int(sum)

if __name__ == '__main__':
    print complement()


