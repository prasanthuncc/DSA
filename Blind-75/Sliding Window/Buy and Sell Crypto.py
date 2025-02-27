"""
Buy and Sell Crypto
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100


"""


def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    for i in range(len(prices)):
        j = i + 1
        while j < len(prices) and prices[i] < prices[j]:
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
            j += 1
    return max_profit


def maxProfit_optimal(prices: list[int]) -> int:
    max_profit = 0
    l = r = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit


if __name__ == '__main__':
    print(maxProfit(prices=[10, 8, 7, 5, 2]))
    print(maxProfit(prices=[10, 1, 5, 6, 7, 1]))
