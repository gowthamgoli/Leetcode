def generateParenthesis(n):
    result = []
    def generateParenthesis_wrapper(parans, left, right, n):
        if left == 0 and right == 0:
            result.append(parans)
            return
        
        if left > 0:
            generateParenthesis_wrapper(parans + '(', left - 1, right, n)
        if left < right:
            generateParenthesis_wrapper(parans + ')', left, right - 1, n)

    generateParenthesis_wrapper('', n, n, n)
    return result

if __name__ == '__main__':
    result = generateParenthesis(3)
    print(result)