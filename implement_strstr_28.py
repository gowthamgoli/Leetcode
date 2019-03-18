def strStr(haystack, needle):
    len_n = len(needle)
    len_h = len(haystack)
    for i in range(0, len_h - len_n + 1):
        if haystack[i: i + len_n] == needle:
            return i
    return -1

if __name__ == '__main__':
    print(strStr("aaaaa", "nba"))