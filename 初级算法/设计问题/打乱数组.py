'''
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 等可能 的。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果
'''
from random import shuffle as sf
class Solution:

    def __init__(self, nums: list[int]):
        self.L = nums

    def reset(self) -> list[int]:
        return self.L

    def shuffle(self) -> list[int]:
        L = self.L[:]
        sf(L)
        return L

S = Solution([1, 2, 3])
print(S.shuffle())
print(S.reset())
print(S.shuffle())