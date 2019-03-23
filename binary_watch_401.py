def readBinaryWatch(num):
    times = []
    for i in range(12):
        bin_i = bin(i)
        for j in range(60):
            num_ones = (bin_i + bin(j)).count('1')
            if num_ones == num: times.append( f'{str(i)}:{str(j).zfill(2)}' )
    return times

if __name__ == '__main__':
    times = readBinaryWatch(0)
    print(times)
    times = readBinaryWatch(5)
    print(times)