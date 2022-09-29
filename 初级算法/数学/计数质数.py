'''
给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
'''
import math

# 朴素解法，但是超时
def countPrimes(n: int) -> int:
    def is_prime(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    cnt = 0
    for i in range(2, n):
        if is_prime(i):
            cnt += 1
    return cnt

# 埃拉托斯特尼 埃氏筛选法 将所有素数的倍数标记为合数
def countPrimes_V2(n: int) -> int:
    is_prime = [True] * n
    cnt = 0
    for i in range(2, n):
        if is_prime[i]:
            cnt += 1
            for j in range(i*i, n, i):
                is_prime[j] = False
    return cnt

ans = countPrimes_V2(5000000)
ans