'''
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
'''
from tree import *
def sortedArrayToBST(nums: list[int]) -> Optional[TreeNode]:
    def inorderT(left, right):
        if left > right:
            return None
        mid = (right + left) // 2
        root = TreeNode(nums[mid])
        root.left = inorderT(left, mid - 1)
        root.right = inorderT(mid + 1, right)
        return root
    return inorderT(0, len(nums) - 1)


ans = sortedArrayToBST([-10,-3,0,5,9])
ans
