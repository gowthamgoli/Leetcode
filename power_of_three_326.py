import math
def isPowerOfThree(n):
    if n <= 0: return False
    x =  math.log10(n) / math.log10(3)
    return x == int(x)

if __name__ == '__main__':
    print(isPowerOfThree(243))