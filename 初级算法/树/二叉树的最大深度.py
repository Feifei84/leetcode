'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
'''

from tree import *

def maxDepth(root: Optional[TreeNode]) -> int:
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

T = makeTree([3,9,20,None,None,15,7])
ans = maxDepth(T)
ans