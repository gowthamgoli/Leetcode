def merge(intervals):
    output = []
    intervals = sorted(intervals, key=lambda k: (k[0], k[1]))
    for i, interval in enumerate(intervals):
        if i == 0: 
            output.append(interval)
            continue
        last_interval = output[-1]
        if interval[0] <= last_interval[1]:
            output[-1] = [min(last_interval[0], interval[0]), max(last_interval[1], interval[1])]
        else:
            output.append(interval)
    print(output)
    return output

if __name__ == "__main__":
    # merge([[2,6],[1,3],[8,10],[16,17],[15,18], [2,9]])
    # merge([[1,3],[2,6],[8,10],[15,18]])
    merge([[1,4],[2,3]])
