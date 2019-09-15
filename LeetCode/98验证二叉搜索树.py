class Solution(object):
    def isValidBST(self, root):
        def judge(node,lower = float('-inf'),upper = float('inf')):
            if not node:
                return True
            val = node.val
            if val<= lower or val >=upper:
                return False
            if not judge(node.right,val,upper):
                return False
            if not judge(node.left,lower,val):
                return False
            return True
        return judge(root)
        """