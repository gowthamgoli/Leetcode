def longestCommonPrefix(strs):
    if len(strs) == 0: return ''
    if len(strs) == 1: return strs[0]
    
    output = longestCommonPrefix(strs[1:])
    s1 = strs[0]
    s2 = output
    result = ''
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]: result += s1[i]
        else: return result
    return result

if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))