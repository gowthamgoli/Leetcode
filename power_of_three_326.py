import math
def isPowerOfThree(n):
    if n <= 0: return False
    if n == 1: return True
    
    return n % 3 == 0 and isPowerOfThree(n / 3)

if __name__ == '__main__':
    print(isPowerOfThree(4))