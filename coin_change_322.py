def coinChange(coins, amount):
    if len(coins) == 0: return -1
    change = [1 << 31] * (amount + 1)
    change[0] = 0
    coins = sorted(coins)
    for i in range(1, amount + 1):
        for coin in coins:
            if coin > amount: break
            change[i] = min(change[i], 1 + change[i - coin])
    return -1 if change[amount] == 1 << 31 else change[amount]

if __name__ == "__main__":
    print(coinChange([1, 2, 5], 11))
    print(coinChange([5], 11))