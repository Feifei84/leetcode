'''
给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
'''

def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    if n == 0:
        return 0
    dp = [0] * n
    minprice = prices[0]
    for i in range(1, n):
        minprice = min(minprice, prices[i])
        dp[i] = max(dp[i - 1], prices[i] - minprice)
    return dp[-1]

# def maxProfit_V2(prices: list[int]) -> int:
#     dp = [[0]]
#     for i in range(1, len(prices)):
#         dp[0].append(max(dp[0][i-1], prices[i] - prices[0]))
#     for i in range(1, len(prices) - 1):
#         dp.append([])
#         for j in range(0, len(prices) - i):
#             if j == 0:
#                 dp[i].append(0)
#             else:
#                 dp[i].append(max(dp[i][j - 1], dp[i - 1][j + 1], prices[j + i] - prices[i]))
#     return dp[-1][-1]

def maxProfit_V3(prices: list[int]) -> int:
    inf = int(1e9)
    minprice = inf
    maxprofit = 0
    for price in prices:
        maxprofit = max(price - minprice, maxprofit)
        minprice = min(price, minprice)
    return maxprofit


ans = maxProfit_V2([4,1,5,2,6,7])
ans