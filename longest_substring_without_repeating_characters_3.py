def lengthOfLongestSubstring(s):
    left, right = 0, 0

    len_longest_sub_string = 0
    longest_sub_string = ''
    map_chars_in_window = {}
    while right < len(s):
        char_at_right = s[right] 
        window_size = right - left + 1
        # print(s[left: right + 1])
        map_chars_in_window[char_at_right] = 1 + map_chars_in_window.get(char_at_right, 0)
        if map_chars_in_window[char_at_right] > 1:
            while left <= right and map_chars_in_window[char_at_right] > 1:
                # print(s[left: right + 1])
                char_at_left = s[left]
                map_chars_in_window[char_at_left] -= 1
                left += 1
        else:
            # print(window_size, len_longest_sub_string)
            if window_size > len_longest_sub_string:
                len_longest_sub_string = window_size
                longest_sub_string = s[left: right + 1]

        right += 1

    return longest_sub_string

if __name__ == '__main__':
    res = lengthOfLongestSubstring('abcabcbb')
    print(res)
    res = lengthOfLongestSubstring('bbbbbb')
    print(res)
    res = lengthOfLongestSubstring('pwwkew')
    print(res)
    res = lengthOfLongestSubstring('nfpdmpi')
    print(res)