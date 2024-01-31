def maxProfitStrategy(prices: [int]) -> (int, int):
    l, r = 0, 1
    maxProfit = 0
    maxProfitL, maxProfitR = l, r

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
            if maxProfit == profit:
                maxProfitL = l
                maxProfitR = r
        else:
            l = r
    
        r += 1

    return (maxProfitL, maxProfitR)

def process(prices: [int]):
    strategy = maxProfitStrategy(prices)
    print(f'maximum profit possible for {prices} by buying at {prices[strategy[0]]} and selling at {prices[strategy[1]]}, yielding a profit of {prices[strategy[1]] - prices[strategy[0]]}.\n')

process([5, 9, 3, 8, 1, 7])
process([3, 6, 1, 6])
process([3, 6, 1, 5])