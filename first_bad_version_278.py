bad_versions = [0, 0, 0, 1, 1, 1, 1]

def isBadVersion(n):
    return bool(bad_versions[n - 1])

def firstBadVersion(n):
    high = n
    low = 1
    while(low < high):
        mid = (low + high) // 2
        print(low, high, mid)
        if not isBadVersion(mid):
            low = mid + 1
        else:
            high = mid
    return low
    
if __name__ == '__main__':
    print(firstBadVersion(7))
