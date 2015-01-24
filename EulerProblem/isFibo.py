'''
You are given an integer, N. Write a program to determine if N is an element of the Fibonacci Sequence.
'''

import sys

def isFibo():
    list = []
    num = int(raw_input())
    for i in range(0,num):
        i = int(raw_input())
        list.append(i)
    for next in list:
        if next in fibonacci():
            print 'IsFibo'
        else:
            print 'IsNotFibo'

def fibonacci():
    fib0 = 0
    fib1 = 1
    fib = fib0 + fib1
    list = []
    list.append(fib1)
    list.append(fib)
    while(fib < 10000000000):
        fib0 = fib1
        fib1 = fib
        fib = fib0 + fib1
        list.append(fib)
    return list

if __name__ == '__main__':
    isFibo()


