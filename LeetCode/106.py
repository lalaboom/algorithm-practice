class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None
        root = postorder[-1]
        res = TreeNode(root)
        i = inorder.index(root)
        res.left = self.buildTree(inorder[:i],postorder[:i])
        res.right = self.buildTree(inorder[i+1:],postorder[i:len(postorder)-1])
        return res