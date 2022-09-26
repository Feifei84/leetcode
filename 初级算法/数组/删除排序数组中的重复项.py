'''
给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。

由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么nums的前 k 个元素应该保存最终结果。

将最终结果插入nums 的前 k 个位置后返回 k 。

不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

'''
def removeDuplicates(nums: list[int]) -> int:
    i = 0
    while i < len(nums) - 1:
        left = nums[i]
        right = nums[i+1]
        while left == right:
            nums.pop(i)
            if i < len(nums) - 1:
                right = nums[i + 1]
            else:
                break
        i += 1
    return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)


def removeDuplicates_S(nums: list[int]) -> int:
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i]
    return len(nums)

