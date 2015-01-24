'''
User enters an arithmetic progression, with one item omitted, and the length of the input, the
program tells the omitted item
'''

import sys
import numpy as np


def solution1():
    n = int(raw_input())
    list= raw_input().split()
    for i in range(0,n):
        list[i] = int(list[i])
    difference = list[len(list)-1] - list[0]
    progression = difference / n

    for i in range(0,len(list)-1):
        if (list[i+1] != list[i] + progression):
            print str(list[i] + progression)


def main():
    solution1()

if __name__ == '__main__':
    main()
