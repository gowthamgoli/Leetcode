def maxProfit(prices):
    if len(prices) in [0, 1]: return 0
    max_profit = 0
    profit = prices[1] - prices[0]
    min_element = prices[0]
    for i in range(1, len(prices)):
        profit = prices[i] - min_element
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_element:
            min_element = prices[i]
    return max_profit

if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,5,4,3,2,1]))
    print(maxProfit([7,8]))
    print(maxProfit([]))
