'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。
'''
from tree import *
# 第一想法是中序遍历后判断是否回文
# 然而在某些情况下这种方法会失效（如[1,2,2,2,None,2]）
# 因此只能严格对比左右子树是否完全相同

# 递归版

def isSymmetric(root: Optional[TreeNode]) -> bool:
    def comp(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and comp(left.left, right.right) and comp(left.right, right.left)
    return comp(root, root)

# 迭代版 层次遍历
def isSymmetric_V2(root: Optional[TreeNode]) -> bool:
    queue = [root]
    while (queue):
        next_queue = list()
        layer = list()
        for node in queue:
            if not node:
                layer.append(None)
                continue
            next_queue.append(node.left)
            next_queue.append(node.right)

            layer.append(node.val)

        if layer != layer[::-1]:
            return False
        queue = next_queue

    return True

T = makeTree([1,2,2,None,3,None,3])
ans = isSymmetric_V2(T)
ans
