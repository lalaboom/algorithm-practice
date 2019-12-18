# 实际上就是改良了“前序遍历”，“前序遍历”是“先自己，再左子树（如果有的话），再右子树（如果有的话）”。

# 而我们改过以后是：“先自己，再右子树（如果有的话），再左子树（如果有的话）”
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(node, res, depth):
            if node is None:
                return
            if len(res) == depth:
                res.append(node.val)
            dfs(node.right, res, depth + 1)
            dfs(node.left, res, depth + 1)

        res = []
        dfs(root, res, 0)
        return res