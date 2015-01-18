__author__ = 'yitongwang'

def SSdifference(n):
    sumSquare = 0
    sum = 0
    for i in range(1,n+1):
        sumSquare += i**2
        sum += i
    return (sum**2 - sumSquare)

if __name__ == '__main__':
    n = raw_input('limit?')
    print SSdifference(int(n))