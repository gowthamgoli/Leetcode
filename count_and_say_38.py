def countAndSay(n):

    def countAndSayHelper(s):
        if len(s) == 1: return f'1{s}'
        output = ''
        prev_char = s[0]
        current_count = 1
        for i in range(1, len(s)):
            current_char = s[i]
            if current_char == prev_char:
                current_count += 1
            else:
                output += f'{current_count}{prev_char}'
                current_count = 1
            prev_char = current_char
        output += f'{current_count}{current_char}'
        return output

    output = '1'
    for i in range(0, n-1):
        output = countAndSayHelper(output)

    return output


if __name__ == '__main__':
    n = 1

    print(countAndSay(4))

