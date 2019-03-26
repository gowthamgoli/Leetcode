def longestPalindrome(s):
    n = len(s)
    p =  [ [0 for i in range(n) ] for i in range(n) ]
    longest_indices = (-1, -1)
    longest_length = -1
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            current_length = j - i + 1
            if i > j: continue
            if i == j: 
                p[i][i] = 1
            elif j == i + 1:
                p[i][i+1] = 1 if s[i] == s[i+1] else 0
            else:
                p[i][j] = 1 if p[i+1][j-1] == 1 and s[i] == s[j] else 0
            if p[i][j] == 1 and current_length > longest_length:
                longest_length = current_length
                longest_indices = (i, j)
    return s[longest_indices[0]: longest_indices[1] + 1]

def longestPalindrome2(s):
    n = len(s)
    max_palin = ''
    for i in range(n):
        for j in range(n-1, i-1, -1):
            window_len = j - i + 1
            window_s = s[i: j + 1]
            # print(i, j, window_s)
            if window_s == window_s[::-1] and window_len > len(max_palin):
                max_palin = window_s
                continue
    return max_palin

            # print(i, j, window_s)

if __name__ == '__main__':
    print(longestPalindrome2('bbabad'))
    print(longestPalindrome('cbbd'))
    print(longestPalindrome('abcd'))
    print(longestPalindrome('a'))