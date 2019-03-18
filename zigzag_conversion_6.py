def convert(s, numRows):
    if numRows == 1: return s
    rows = numRows
    i = 0
    cols = 0
    digonal = numRows - 2
    zig = True
    while i < len(s):
        if zig:
            i += numRows
            cols += 1
            zig = False  
        else:
            i += numRows - 2
            cols += numRows - 2
            zig = True
    
    zig_zag = [ [ '' for i in range(cols)] for i in range(rows) ]
    i, j, zig = 0, 0, True
    ptr = 0
    while ptr < len(s):
        zig_zag[i][j] = s[ptr]
        
        if i == rows - 1:
            zig = False
        if i == 0:
            zig = True

        if zig: i += 1
        else: 
            i -= 1
            j += 1
        ptr += 1
    outputs = []
    for i in range(rows):
        # print(zig_zag[i])
        outputs.append((''.join(zig_zag[i])).strip())
    print(''.join(outputs))
    return '\n'.join(outputs)

if __name__ == '__main__':
    # convert('PAYPALISHIRING', 3)
    # convert('PAYPALISHIRING', 4)
    convert('PAYPALISHIRING', 2)
    print(convert('AB', 1))