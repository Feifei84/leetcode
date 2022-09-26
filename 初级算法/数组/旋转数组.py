'''
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
'''
def rotate(nums: list[int], k: int) -> None:
    # nums = nums[::-1]不是原地操作 nums[:] = nums[::-1]是原地操作
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    ## 或 nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

a = [1,2,3,4,5,6,7]
rotate(a, 3)