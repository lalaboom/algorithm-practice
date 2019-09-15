class Solution(object):
    def isSymmetric(self, root):
        def match(l,r):
            if not l and not r:return True
            if not l or not r: return False
            return l.val==r.val and match(l.left, r.right) and \
                match(l.right, r.left)
        return match(root,root)
        
        """
        :type root: TreeNode
        :rtype: bool
        """
#     构建一个 match() 函数，通过深度优先遍历DFS判断是否为对称二叉树，思路是在遍历过程中，每次对比当前点与对称点的值是否相等。
# 参数：
# 节点l节点r，每轮递归比较两节点值是否相等l.val == r.val；
# 返回值：
# 节点l和r值是否相等 且
# 节点l的左子树和节点r右子树是否对称 且
# 节点l的右子树和节点r左子树是否对称
# 终止条件：
# 节点l和r同时为null则返回true，代表同时越过叶子节点，以上全部值相同；
# 节点l和r有一个为null则返回false，代表只有一边越过叶子节点，意味着树不对称。