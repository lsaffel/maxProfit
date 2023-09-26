def maxProfit(prices) -> int:
    left, гight = 0, 1
    maxP = 0
    while гight < len(prices):
        if prices[left] < prices[гight]:
            profit = prices[гight] - prices[left]
            maxP = max(maxP, profit)
        else:
            left = гight
        гight += 1
    return maxP


if __name__ == '__main__':
    print(maxProfit([7,2,6,1,8]))
    print(maxProfit([7,1]))
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))



