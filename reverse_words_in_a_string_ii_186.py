def reverseWords(str):
    def reverseString(s, start, end):
        for i in range((end - start + 1) // 2):
            s[start + i], s[end - i] = s[end - i], s[start + i]
    start, end = 0, 0
    n = len(str)
    reverseString(str, 0, n - 1)
    while start < n and end < n:
        if end + 1 < len(str) and str[end + 1] == ' ':
            reverseString(str, start, end)
            start = end + 2
            end = end + 2
            continue
        end += 1
    reverseString(str, start, len(str) - 1)

if __name__ == "__main__":
    reverseWords(["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"])
    # reverseWords(["t", "h", "e", " ", "x"])
