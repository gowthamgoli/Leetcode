def fizzBuzz(n):
    output = []
    for i in range(1, n+1):
        result = ''
        if i % 3 == 0: result += 'Fizz'
        if i % 5 == 0: result += 'Buzz'
        result = result or str(i)
        output.append(result)
    return output

if __name__ == '__main__':
    print(fizzBuzz(15))