'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
# 类斐波那契数列
# 递归 or 动态规划

def climbStairs(n: int) -> int:
    # 递归 超时
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n-1) + climbStairs(n-2)

def climbStairs_V2(n: int) -> int:
    # 改用动态规划
    dp = [1, 2]
    for i in range(2, n):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n-1]

def climbStairs_V3(n: int) -> int:
    # 优化空间复杂度
    if n == 1:
        return 1
    if n == 2:
        return 2
    x = 1
    y = 2
    for i in range(2, n):
        z = x + y
        x = y
        y = z
    return z



ans = climbStairs_V3(38)
ans