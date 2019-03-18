import math
def reverse(x):
    t = x
    x = abs(x)
    output = 0
    while x > 0:
        output *= 10
        output += x % 10
        x = int(x / 10)
    if output > 1<<31:
        return 0
    return -int(output) if t < 0 else int(output)

def reverse2(x):
    output = 0
    neg = True if x < 0 else False
    x = abs(x)
    while x > 0:
        output = 10 * output + (x % 10)
        x //=  10
    if output > 1<<31:
        return 0
    return -output if neg else output

if __name__ == '__main__':
    print(reverse2(234))
    print(reverse2(-234))
    print(reverse2(40))
    print(reverse2(-400))
    print(reverse2(1534236469))