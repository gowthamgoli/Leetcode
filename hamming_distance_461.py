def hammingDistance(x, y):
    return bin(x ^ y).count('1')

if __name__ == '__main__':
    print(hammingDistance(1, 4))