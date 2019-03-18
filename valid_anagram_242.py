def isAnagram(s, t):
    map_s, map_t = {}, {}
    for c in s: map_s[c] = map_s.get(c, 0) + 1
    for c in t: map_t[c] = map_t.get(c, 0) + 1
    if len(map_s) != len(map_t): return False
    for key, val in map_s.items():
        if key not in map_t: return False
        if map_t[key] != val: return False

    return True

if __name__ == '__main__':
    print(isAnagram('anagram', 'agaram'))