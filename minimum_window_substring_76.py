import sys

def minWindow(s, t):
    map_t_char_count = {}
    for c in t: map_t_char_count[c] = map_t_char_count.get(c, 0) + 1
    total_to_match = len(map_t_char_count)
    matches_so_far = 0
    left, right = 0, 0
    min_window_size = sys.maxsize
    min_window = ''
    map_window_char_count = {}
    while right < len(s):
        char_at_right = s[right]
        map_window_char_count[char_at_right] = map_window_char_count.get(char_at_right, 0) + 1
        if char_at_right in map_t_char_count and map_window_char_count[char_at_right] == map_t_char_count[char_at_right]:
            matches_so_far += 1

        while left <= right and total_to_match == matches_so_far:
            window_size = right - left + 1
            char_at_left = s[left]
            if window_size < min_window_size:
                min_window_size = window_size
                min_window = s[left: right + 1]
            map_window_char_count[char_at_left] -= 1
            if char_at_left in map_t_char_count and map_window_char_count[char_at_left] < map_t_char_count[char_at_left]:
                matches_so_far -= 1
            left += 1
        right += 1

    return min_window

if __name__ == '__main__':
    result = minWindow('ADOBECNODEBANC', 'BANC')
    print(result)
    result = minWindow('ADOBECNODEBANC', 'NOB')
    print(result)