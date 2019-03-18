import math

def countBits(n):
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1: bits[i] = 1
        else:
            bits[i] = 1 + bits[i - int(math.pow(2, int(math.log(i, 2))))]
    return bits

if __name__ == '__main__':
    bits = countBits(5)
    print(bits)