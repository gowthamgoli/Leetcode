def isHappy(n):
    def square_digits(num):
        result = 0
        while num > 0: 
            result += (num % 10) * (num % 10)
            num //= 10
        return result
        
    nums = {}
    nums[n] = 1
    while n != 1:
        print(n)
        n = square_digits(n)
        if n in nums: return False
        nums[n] = 1
    return True

if __name__ == "__main__":
    print(isHappy(19))
    print(isHappy(18))
