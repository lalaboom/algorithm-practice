class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #基于二叉搜索树的特性，直接查找最近的公共祖先。最近公共祖先应该是第一个介于p,q之间的节点
        if p.val >q.val:
            p,q = q,p
        while True:
            if root.val>q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                return root  