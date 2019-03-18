def romanToInt(s):
    output = 0
    prev_char = ''
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i in range(len(s)-1, -1, -1):
        curr_char = s[i]
        # print()
        if prev_char in ['V', 'X'] and curr_char == 'I': output -= 1
        elif prev_char in ['L', 'C'] and curr_char == 'X': output -= 10
        elif prev_char in ['D', 'M'] and curr_char == 'C': output -= 100
        else: output += roman_to_int[curr_char]
        prev_char = curr_char
    return output

if __name__ == '__main__':
    print(romanToInt('MCMXCIV'))
    print(romanToInt('III'))
    print(romanToInt('IV'))