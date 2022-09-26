'''
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
'''

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(1, len(nums)):
        sum_i = [a+b for a, b in zip(nums, nums[len(nums) - i:] + nums[:len(nums) - i])]
        for n, j in enumerate(sum_i):
            if j == target:
                return [n, (len(nums)+n-i) % len(nums)]

def twoSum_V2(nums: list[int], target: int) -> list[int]:
    dcit = {}
    for i in range(len(nums)):
        if target - nums[i] in dcit:
            return [dcit[target - nums[i]], i]
        dcit[nums[i]] = i
    return []

twoSum_V2([3,2,3], 6)