'''
The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, 
when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter. 
Now, a new Utopian tree sapling is planted at the onset of the spring. Its height is 1 meter. 
Can you find the height of the tree after N growth cycles?
'''

import sys
import math

def getIntel():
    num = int(raw_input())
    for i in range(0,num):
        cycle = int(raw_input())
        print getYear(cycle)

def getYear(cyc):
    if (cyc == 0):
        return 1
    elif (cyc == 1):
        return 2
    elif (cyc == 2):
        return 3
    else:
        year = 0
        if (cyc % 2 == 1):
            while(cyc != 1):
                n = cyc / 2
                year = year + math.pow(2,n+1)
                cyc = cyc - 2
            return int(year + getYear(cyc))
        else:
            while(cyc != 2):
                n = cyc / 2
                year = year + math.pow(2,n)
                cyc = cyc - 2
            return int(year + getYear(cyc))





if __name__ == '__main__':
    getIntel()


