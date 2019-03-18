def plusOne(digits):
    output = []
    digits = reversed(digits)
    carry = 1
    for num in digits:
        s = num + carry 
        carry = s // 10
        output.append(s % 10)
    if carry:
        output.append(carry)
    return list(reversed(output))

if __name__ == '__main__':
    print(plusOne([1,2,3]))
    print(plusOne([9, 9, 9]))


