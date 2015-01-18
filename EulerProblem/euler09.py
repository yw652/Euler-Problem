__author__ = 'yitongwang'
'''
for a<b<c, exists one set of a,b,c such that they satisfy the
pythagorean axioms (a**2+b**2=c**2). Find a*b*c
'''

def pythagorean():
    for b in range(2,1000):
        for a in range(1,b):
            if a+b < 1000:
                c = 1000 - a - b
                if (c>b) & (a**2 + b**2 == c ** 2):
                    return a*b*c

if __name__ == "__main__":
    print pythagorean()