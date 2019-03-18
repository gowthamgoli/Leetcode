def findContentChildren(g, s):
    count = 0
    g, s = sorted(g), sorted(s)
    i, j = 0, 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]: 
            count += 1
            i += 1
            j += 1
        else: j+= 1
    return count

if __name__ == '__main__':
    count = findContentChildren([1,2,3], [1,1])
    print(count)
    count = findContentChildren([1,2,3], [1,2])
    print(count)
    count = findContentChildren([1,2], [1,2,3])
    print(count)
