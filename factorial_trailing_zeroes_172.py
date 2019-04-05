def trailingZeroes(n):
    count = 0
    init = 5
    while init <= n:
        count += n // init
        init *= 5
    return count

if __name__ == "__main__":
    print(trailingZeroes(100))
    # print(trailingZeroes(1808548329))