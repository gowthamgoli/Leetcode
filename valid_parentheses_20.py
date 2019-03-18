def isValid(s):
    stack = []
    for c in s:
        if len(stack) == 0 and c in [')', ']', '}']: return False
        if c in ['(', '[', '{']: stack.append(c)
        else:
            opening = stack.pop()
            if opening == '(' and c != ')': return False
            elif opening == '[' and c != ']': return False
            elif opening == '{' and c != '}': return False

    if len(stack) == 0: return True
    return False

if __name__ == '__main__':
    print(isValid(r'()[]{}'))
    print(isValid(r'()'))
    print(isValid(r'([)]'))
    print(isValid(r''))