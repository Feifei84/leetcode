'''
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
'''

def missingNumber(nums: list[int]) -> int:
    sum_all = (1 + len(nums)) * len(nums) // 2
    return sum_all - sum(nums)

ans = missingNumber([9,6,4,2,3,5,7,0,1])
ans