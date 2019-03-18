import math
def intToRoman(num):
    result = ''
    ints = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    int_to_roman = {
        1   : 'I',
        4   : 'IV',
        5   : 'V',
        9   : 'IX',
        10  : 'X',
        40  : 'XL',
        50  : 'L',
        90  : 'XC',
        100 : 'C',
        400 : 'CD',
        500 : 'D',
        900 : 'CM',
        1000: 'M',
    }
    while num > 0:
        i = 0
        while i < len(ints):
            if num // ints[i] < 1:
                i = i - 1
                break
            i += 1
        if i == len(ints): i = len(ints) - 1
        result += int_to_roman[ints[i]] * (num // ints[i])
        num = num % ints[i]
    return result

if __name__ == '__main__':
    print(intToRoman(58))
    print(intToRoman(3000))
    print(intToRoman(1994))
    print(intToRoman(4))