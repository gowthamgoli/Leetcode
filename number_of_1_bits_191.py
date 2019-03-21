def hammingWeight(n):
    return bin(n).count('1')

def hammingWeight2(n):
    count = 0 
    for _ in range(32):
        count += n & 1
        n >>= 1
    return count

if __name__ == '__main__':
    print(hammingWeight(110))
    print(hammingWeight2(110))