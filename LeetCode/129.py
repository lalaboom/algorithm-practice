
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
            self.res = 0
            def helper(root, tmp):
                if not root: return 
                if not root.left and not root.right:
                    self.res += int(tmp + str(root.val))
                    return   
                helper(root.left, tmp + str(root.val))
                helper(root.right, tmp + str(root.val))
            helper(root, "")
            return self.res
