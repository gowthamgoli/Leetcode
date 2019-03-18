def firstUniqChar(s):
    map_char = {}
    for c in s:
        map_char[c] = map_char.get(c, 0) + 1
    for i, c in enumerate(s):
        if map_char[c] == 1: return i
    return -1

if __name__ == '__main__':
    print(firstUniqChar('leetcode'))
    print(firstUniqChar('cc'))

