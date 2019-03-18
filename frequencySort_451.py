def frequencySort(s):
    map_chars = {}
    res = ''
    for c in s:
        map_chars[c] = 1 + map_chars.get(c, 0)
    map_counts = sorted(map_chars.items(), key=lambda x: x[1], reverse=True)     
    for entry in map_counts:
        res += entry[0] * entry[1]
    return res
        
if __name__ == '__main__':
    print(frequencySort('tree'))
