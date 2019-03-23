import re
def isPalindrome(s):
    s2 = ''
    for c in s: s2 += c.lower() if re.match(r'[a-z0-9]', c, re.IGNORECASE) else ''
    for i in range(0, int(len(s2)/2)):
        if s2[i] != s2[len(s2)-i-1]: return False
    return True

if __name__ == '__main__':
    print(isPalindrome('A man, a plan, a canal: Panama'))
    print(isPalindrome('A man, a plan, a canal: Panama'))
    print(isPalindrome('AXY'))