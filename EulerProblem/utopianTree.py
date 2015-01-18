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


