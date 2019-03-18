def letterCombinations(digits):
    letter_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    if len(digits) == 0: return []
    if len(digits) == 1: return list(letter_map[digits])
    comb1 = letterCombinations(digits[0])
    comb2 = letterCombinations(digits[1:])
    output = []
    for s1 in comb1:
        for s2 in comb2:
            output.append(s1 + s2)
    return output

if __name__ == '__main__':
    print(letterCombinations('2'))
    print(letterCombinations(''))