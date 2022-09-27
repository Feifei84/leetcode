'''
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''
from tree import *


# 中序遍历 递归
def isValidBST(root: Optional[TreeNode]) -> bool:
    def inorderT(root):
        if not root:
            return []
        res = []
        res += inorderT(root.left)
        res.append(root.val)
        res += inorderT(root.right)
        return res
    L = inorderT(root)
    for i in range(len(L)-1):
        if L[i] >= L[i+1]:
            return False
    return True
    # return L == sorted(L)

# 官方迭代版
def isValidBST(root: TreeNode) -> bool:
    def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True
    return helper(root)


# 中序遍历 迭代
def isValidBST_V2(root: Optional[TreeNode]) -> bool:
    stack = []
    v = - 2**31 - 1
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if v >= cur.val:
                return False
            v = cur.val
            cur = cur.right
    return True

T = makeTree([5,1,4,None,None,3,6])
ans = isValidBST_V2(T)
ans
