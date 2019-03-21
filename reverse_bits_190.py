def reverseBits(n):
    return int(bin(n)[2:].zfill(32)[::-1], 2)

def reverseBits2(n):
    ans = 0
    for _ in range(32):
        ans = (ans << 1) | (n & 1)
        n >>= 1
    return ans

if __name__ == '__main__':
    print(reverseBits2(23))
    print(reverseBits(23))