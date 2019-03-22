from collections import defaultdict

def groupAnagrams(strs):
    map_s = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        map_s[key].append(s)
    return list(map_s.values())

if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))