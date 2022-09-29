'''
给定一个整数，写一个函数来判断它是否是 3的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3**x
'''

# 要求非递归、循环解决
# n == 3**x 同取对数， 有log n = x * log 3
# log n / log 3 = x
# x 是整数， 即log n / log 3 % 1 == 0

import math

def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False
    # return round(math.log10(n) / math.log10(3), 9) % 1 == 0
    return 1162261467 % n == 0


ans = isPowerOfThree(300)
ans