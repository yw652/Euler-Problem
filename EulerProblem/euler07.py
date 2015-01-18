__author__ = 'yitongwang'


def findPrime(n):
    prime = [2,3,5,7,11,13,17,19,23,29]
    while(len(prime) < n):
        target = prime[-1] + 1
        i = 0
        while(i < len(prime)):
            if (target % prime[i] != 0):
                i += 1
            else:
                target += 1
                i = 0
        prime.append(target)
    print prime
    return prime[-1]

if __name__ == "__main__":
    n = int(raw_input('Position?'))
    print findPrime(n)


