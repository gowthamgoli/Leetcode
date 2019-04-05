def titleToNumber(s):
    init = 1
    output = 0
    for i in range(len(s) - 1, -1, -1):
        bit = ord(s[i]) - ord('A') + 1
        output += init * bit
        init *= 26
    return output

if __name__ == "__main__":
    print(titleToNumber('Z'))    