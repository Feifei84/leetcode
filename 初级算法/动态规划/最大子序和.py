'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
'''

def maxSubArray(nums: list[int]) -> int:
    dp = [nums[0]]
    for i in range(1, len(nums)):
        dp.append(max(dp[i-1] + nums[i], nums[i]))
    return max(dp)

def maxSubArray_V2(nums: list[int]) -> int:
    ans = nums[0]
    cur = nums[0]
    for i in range(1, len(nums)):
        cur = max(cur + nums[i], nums[i])
        ans = max(cur, ans)
    return ans

ans = maxSubArray_V2([-2,1,-3,4,-1,2,1,-5,4])
ans