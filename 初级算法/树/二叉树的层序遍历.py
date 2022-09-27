'''
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
'''
from tree import *
def levelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    queue = [root]
    ans = []
    while (queue):
        next_queue = list()
        layer = []
        for node in queue:
            if not node:
                continue
            next_queue.append(node.left)
            next_queue.append(node.right)

            layer.append(node.val)

        if layer: ans.append(layer)
        queue = next_queue
    return ans

T = makeTree([3,9,20,None,None,15,7])
ans = levelOrder(T)
ans