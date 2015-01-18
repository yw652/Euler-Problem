import numpy as np
'''
Find the sum of all the natural numbers under 1000 who is either divisible by 3 or 5
'''

def findSum():
    '''
    list = []
    for i in range(0,1000):
        if (i % 3 == 0) | (i % 5 == 0) | ((i % 3 == 0) & (i % 3 == 0)):
            list.append(i)
    print sum(list)
    '''

    print sum([x for x in range(0,1000) if ((x % 3 == 0) | (x % 5 == 0))])

if __name__ == '__main__':
    findSum()
