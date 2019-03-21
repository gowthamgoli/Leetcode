def generate(numRows):
    output = []
    def get_row(n):
        coeff = 1
        power = n
        term = 1
        result = [coeff]
        for i in range(n, 0, -1):
            coeff = int((coeff * power) / term)
            term += 1
            power -= 1
            result.append(coeff)
        # print(result)
        return result

    for i in range(0, numRows):
        output.append(get_row(i))
    return output

if __name__ == '__main__':
    generate(5)