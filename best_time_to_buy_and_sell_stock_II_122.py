def maxProfit(prices):
    profit = 0
    if len(prices) < 2: return profit
    
    i = 0
    j = 0
    # buy, sell = 0, 0
    # current_min = prices[0]
    while i < len(prices) and j < len(prices):
        while (j + 1) < len(prices) and prices[j] <= prices[j + 1]:
            j += 1
        if i == j:
            i += 1
            j += 1
            continue
        buy = i
        sell = j
        profit += prices[sell] - prices[buy]
        i = sell + 1
        j = i
        
    # current_profit = 0
    # current_min = prices[0]
    # for i in range(1, len(prices)):
    #     stock_val = prices[i]
    #     if stock_val - current_min > current_profit:
    #         current_profit = stock_val - current_min
    #     else:
    #         profit += current_profit
    #         current_profit = 0
    #         current_min = prices[i]
    #         print(current_profit, current_min)
    #     current_min = min(current_min, prices[i])

    return profit

if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([1,2,3,4,5]))
    print(maxProfit([10, 9, 8, 7, 6, 10]))