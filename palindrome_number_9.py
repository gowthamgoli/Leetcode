def isPalindrome(x):
    if x < 0: return False
    # if x // 10 == 0: return True
    div = 1
    while x // div >= 10:
        div *= 10
    
    while x != 0:
        # if x // 10 == 0: return True
        e = x % 10
        s = x // div
        if s != e: return False
        x = (x % div) // 10
        div //= 100
    return True

if __name__ == '__main__':
    print(isPalindrome(1000021))
    print(isPalindrome(22))
