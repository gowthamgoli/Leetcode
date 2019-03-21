import math

def countPrimes(n):
    def isPrime(k):
        p = int(math.sqrt(k))
        for i in range(2, p + 1):
            if k % i == 0: return False
        return True
    output = []
    for i in range(2, n):
        if isPrime(i): output.append(i)
    return len(output)

if __name__ == '__main__':
    print(countPrimes(10))