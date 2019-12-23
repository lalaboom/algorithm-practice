# 记录每一行最左边的节点，然后用next来比拟队列的连接即可、
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        def helper(root, depth):
            if not root: return 
            if len(res) == depth:
                res.append([])
            if depth % 2 == 0:res[depth].append(root.val)
            else: res[depth].insert(0, root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return res
