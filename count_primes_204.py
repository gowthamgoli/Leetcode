import math

def countPrimes(n):
    output = 0
        if n in [0, 1]: return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, n // 2 + 1):
            if primes[i] == 0: continue
            for j in range(i * i, n, i):
                primes[j] = 0
        for i in range(2, n): output += primes[i]
        return output

if __name__ == '__main__':
    print(countPrimes(39))