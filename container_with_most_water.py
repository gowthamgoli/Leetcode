def maxArea(height):
    max_area = 0
    i, j = 0, len(height) - 1
    while i < j:
        max_area = max((j - i) * min(height[i], height[j]), max_area)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))