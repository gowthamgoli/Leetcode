import re 

def myAtoi(s):
    matches = re.search(r'^\s*[-+]?\d+', s)
    if matches is None: return 0
    INT_MAX = (1 << 31) - 1
    INT_MIN = -(1 << 31)

    num = matches.group(0).strip()
    if num.startswith('-'): 
        sign = '-'
        num = num[1:]
    elif num.startswith('+'): 
        sign = '+'
        num = num[1:]
    else:
        sign = '+'
    
    result = 0
    for c in num:
        result = result * 10 + int(c)
    result = -result if sign == '-' else result
    if result > INT_MAX: return INT_MAX
    if result < INT_MIN: return INT_MIN
    return result

if __name__ == '__main__':
    print(myAtoi('  -987'))
    print(myAtoi('-'))